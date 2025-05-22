import * as welcome from './generated/welcome_pb.js';
import * as shared_architecture from './generated/shared_architecture_pb.js';

// Constants for device states and receiver types
export const DeviceState = {
  0: 'LOADING',
  1: 'DISABLED',
  2: 'UNAVAILABLE',
  3: 'READY',
  4: 'BUSY',
  5: 'MEASURING',
  6: 'TYPE_MISMATCH',
  7: 'OFFLINE',
  8: 'IS_MANUAL_DEVICE',
  9: 'NOT_INITIALIZED',
  10: 'BUSY_MEASURING',
  11: 'PREPARING_TO_MEASURE'
};

export const ReceiverType = {
  0: 'SIGNAL_SHARK',
  1: 'ESMD',
  2: 'EB500',
  3: 'DDF205',
  4: 'DDF255',
  5: 'ESMB',
  6: 'EB200',
  7: 'EM200',
  8: 'PR200'
};



export class ApiClient {
  constructor(baseUrl = 'http://localhost:9090') {
    this.baseUrl = baseUrl;
    this.token = null;
  }

  async handshake(deviceId, username = '', serverToken = '', isGuestUser = false, deviceIp, devicePort) {
    let fulldeviceId = deviceId;
    if (!deviceId.startsWith('device')) {
      fulldeviceId = `device${deviceId}`;
    }
    const response = await fetch(`${this.baseUrl}/api/v1/handshake`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-device-id': fulldeviceId,
        'x-device-ip': deviceIp,
        'x-device-port': devicePort.toString(),
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        username,
        serverToken,
        isGuestUser
      })
    });

    if (!response.ok) {
      throw new Error(`Handshake failed: ${response.statusText}`);
    }

    const data = await response.json();

    this.token = data.frontend_token;
    console.log('Handshake response:', data, this.token);
    return this.token;
  }


  streamReceiverList(deviceId, onData, onError,
    deviceIp, devicePort, token) {
    const id = deviceId.startsWith("device") ? deviceId : `device${deviceId}`;

    const url = `${this.baseUrl}/api/v1/receivers/stream?deviceId=${id}`;

    // gRPC metadata → plain HTTP headers
    const headers = {
      "Content-Type": "application/json",   // required by transcoder
      "x-device-id": id,                      // match backend expectation
      "x-device-ip": deviceIp,
      "x-device-port": String(devicePort),
      "token": this.token                                // <- header name is literally “token”
    };

    const ctrl = new AbortController();

    fetch(url, {
      method: "POST",        // <-- must be POST for this RPC
      headers,
      body: "{}",            // google.protobuf.Empty in JSON form
      credentials: "omit",
      signal: ctrl.signal,
    })
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        console.log("stream opened", res);

        const reader = res.body.getReader();
        const dec = new TextDecoder();
        let buf = "";

        const pump = () =>
          reader.read().then(({ done, value }) => {
            if (done) return;

            try {
              // gRPC-Web: first byte is flags, next 4 bytes is message length (big-endian)
              if (value.length < 5) throw new Error("Frame too short");
              const msgLen = (value[1] << 24) | (value[2] << 16) | (value[3] << 8) | value[4];
              const msgBytes = value.slice(5, 5 + msgLen);

              // Make sure shared_architecture is initialized before use
              if (!welcome.proto.shared_architecture) {
                welcome.proto.shared_architecture = shared_architecture.proto.shared_architecture;
              }

              const message = welcome.proto.welcome_grpc.ReceiverListGrpc.deserializeBinary(msgBytes);
              const receivers = message.getReceiversList().map(r => ({
                all: r.toObject(),
                id: r.getId(),
                name: r.getName().getValue(),
                state: DeviceState[r.getState()] ?? "UNKNOWN",
                type: ReceiverType[r.getType()] ?? "UNKNOWN",
              }));
              onData(receivers);
            } catch (e) {
              console.error('Stream error details:', e);
              onError?.(e);
            }

            pump();
          })
            .catch((e) => (e.name !== "AbortError") && onError?.(e));

        pump();
      })
      .catch((e) => onError?.(e));

    return { cancel: () => ctrl.abort() };
  }


  streamReceiverList1(deviceId, onData, onError, deviceIp, devicePort) {
    // Ensure deviceId has the 'device' prefix
    const formattedDeviceId = deviceId.startsWith('device') ? deviceId : `device${deviceId}`;
    console.log('Formatted deviceId:', formattedDeviceId);
    console.log('Device IP:', deviceIp);
    console.log('Device Port:', devicePort);
    console.log('Starting stream...');
    const url = new URL(`${this.baseUrl}/api/v1/receivers/stream`);
    url.searchParams.append('deviceId', formattedDeviceId);

    // Create headers object for fetch
    const headers = new Headers({
      'x-device-id': formattedDeviceId,
      'x-device-ip': deviceIp,
      'x-device-port': devicePort.toString()
    });

    if (this.token) {
      headers.append('Authorization', `Bearer ${this.token}`);
    }
    console.log('Headers:', headers);
    console.log('URL:', url.toString());

    // Use fetch to create a streaming connection with headers
    fetch(url.toString(), {
      method: 'GET',
      headers: headers,
      credentials: 'omit'
    }).then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const reader = response.body.getReader();
      const decoder = new TextDecoder();

      function readStream() {
        reader.read().then(({ done, value }) => {
          if (done) {
            console.log('Stream complete');
            return;
          }
          try {
            const chunk = decoder.decode(value);
            const lines = chunk.split('\n');
            lines.forEach(line => {
              if (line.startsWith('data:')) {
                const data = JSON.parse(line.slice(5));
                onData(data.receivers.map(receiver => ({
                  id: receiver.id,
                  name: receiver.name,
                  state: DeviceState[receiver.state] || 'UNKNOWN',
                  type: ReceiverType[receiver.type] || 'UNKNOWN'
                })));
              }
            });
          } catch (error) {
            console.error('Error parsing SSE data:', error);
            if (onError) onError(error);
          }
          readStream();
        }).catch(error => {
          console.error('Stream error:', error);
          if (onError) onError(error);
        });
      }

      readStream();
    }).catch(error => {
      console.error('Connection error:', error);
      if (onError) onError(error);
    });

    return {
      cancel: () => {
        console.log('Closing stream connection');
        // The fetch API doesn't provide a direct way to cancel streams
        // but the connection will be closed when the component unmounts
      }
    };
  }

  // Add other API methods as needed...

  destroy() {
    // Cleanup if needed
  }
}
import { SimpleModeGrpcClient } from './generated/simple_mode_grpc_grpc_web_pb';
import { 
  SimpleModeMeasurementConfig,
  SimpleModeMeasuringRequest,
  AudioStreamingRequest,
  FrequencyUpdateRequest,
  SimpleHandshakeRequest
} from './generated/simple_mode_grpc_pb';
import { Empty } from 'google-protobuf/google/protobuf/empty_pb';

export class GrpcClient {
  constructor(envoyUrl) {
    this.client = new SimpleModeGrpcClient(envoyUrl);
  }

  // ... existing methods ...

  // Stream receivers data
  streamReceivers(deviceId, token, callback) {
    const request = new Empty();

    const metadata = {
      'authorization': `Bearer ${token}`,
      'x-device-id': deviceId
    };

    const stream = this.client.streamReceivers(request, metadata);
    
    stream.on('data', (response) => {
      callback(response.toObject());
    });

    stream.on('error', (error) => {
      console.error('Receiver stream error:', error);
    });

    stream.on('end', () => {
      console.log('Receiver stream ended');
    });

    return stream;
  }
}

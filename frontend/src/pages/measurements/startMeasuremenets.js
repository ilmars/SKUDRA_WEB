import { GrpcClient } from '@/grpc/client';

// In your component
const client = new GrpcClient('http://localhost:8080'); // Envoy URL

// Example usage
async function startMeasurement() {
  try {
    // First handshake
    const handshakeResponse = await client.simpleHandshake(
      deviceId,
      username,
      serverToken
    );

    // Start measurement stream
    const stream = client.streamMeasurements(
      deviceId,
      handshakeResponse.frontendToken,
      {
        frequency: 100.5,
        measuringMode: 1, // Use appropriate enum value
        bandwidthType: { requirement: 1 }, // Use appropriate enum value
        polarization: { requirement: 1 } // Use appropriate enum value
      },
      (data) => {
        console.log('Received measurement:', data);
      }
    );

    // Later, to stop
    await client.stopMeasuring(deviceId, handshakeResponse.frontendToken);
  } catch (error) {
    console.error('Error:', error);
  }
}

# SKUDRA WEB Backend API Documentation

## Authentication Endpoints

### `/api-auth/`
- `GET /api-auth/login/` - Login page for REST framework browsable API
- `GET /api-auth/logout/` - Logout endpoint

### `/api/user/`
- `GET /api/user/` - Get current authenticated user information
  - Returns: username, full_name, groups, isAdmin status
  - Requires: Authentication

## Configuration Endpoints

### `/api/config/`
- `GET /api/config/` - Get system configuration
  - Returns: site_name, maintenance_mode, map settings, OAuth2 settings
  - Requires: Authentication

## Sensor Management Endpoints

### `/api/sensors/`
- `GET /api/sensors/` - List all sensors
  - Optional query params:
    - `receivers=false` - Exclude receiver data from response
  - Returns: List of sensors with their properties (ip, port, driver_name, state, location, etc.)
  - Requires: Authentication

- `POST /api/sensors/` - Create a new sensor
  - Body: Sensor data (ip, port, driver_name, location)
  - Returns: Created sensor object
  - Requires: Authentication

### `/api/sensors/{id}/`
- `GET /api/sensors/{id}/` - Get specific sensor details
  - Returns: Detailed sensor information including receivers
  - Requires: Authentication

- `PUT /api/sensors/{id}/` - Update sensor
  - Body: Updated sensor data
  - Returns: Updated sensor object
  - Requires: Authentication

- `DELETE /api/sensors/{id}/` - Delete sensor
  - Requires: Authentication

### `/api/receivers/`
- `GET /api/receivers/` - List all receivers
  - Returns: List of receivers with their properties (guid, name, state, type, sensor_id)
  - Requires: Authentication

### `/api/session-tokens/`
- `GET /api/session-tokens/` - List sensor session tokens
  - Returns: List of active session tokens
  - Requires: Authentication

## gRPC Endpoints (Port 9090)

### Handshake Protocol
```javascript
const client = new ApiClient('http://localhost:9090');

// Initialize connection with sensor
const token = await client.handshake(
  deviceId,      // e.g., "device1" or "1"
  username,      // optional
  serverToken,   // optional
  isGuestUser,   // boolean
  deviceIp,      // e.g., "10.0.0.1"
  devicePort     // e.g., 19010
);
```

### Streaming Receiver List
```javascript
const stream = client.streamReceiverList(
  deviceId,          // Sensor ID
  (receivers) => {   // Data callback
    // Receiver format:
    // {
    //   id: string,
    //   name: string,
    //   state: "READY" | "BUSY" | "DISABLED" | etc,
    //   type: "SIGNAL_SHARK" | "ESMD" | "EB500" | etc
    // }
    console.log('Received receivers:', receivers);
  },
  (error) => {       // Error callback
    console.error('Stream error:', error);
  },
  deviceIp,          // Sensor IP address
  devicePort         // Sensor port number
);

// Stop streaming
stream.cancel();
```

### Device States
Available device states for receivers:
```javascript
const DeviceState = {
  LOADING: 0,
  DISABLED: 1,
  UNAVAILABLE: 2,
  READY: 3,
  BUSY: 4,
  MEASURING: 5,
  TYPE_MISMATCH: 6,
  OFFLINE: 7,
  IS_MANUAL_DEVICE: 8,
  NOT_INITIALIZED: 9,
  BUSY_MEASURING: 10,
  PREPARING_TO_MEASURE: 11
};
```

### Receiver Types
Available receiver types:
```javascript
const ReceiverType = {
  SIGNAL_SHARK: 0,
  ESMD: 1,
  EB500: 2,
  DDF205: 3,
  DDF255: 4,
  ESMB: 5,
  EB200: 6,
  EM200: 7,
  PR200: 8
};
```

### Error Handling
```javascript
try {
  const token = await client.handshake(deviceId, username, serverToken, false, deviceIp, devicePort);
} catch (error) {
  console.error('Handshake failed:', error.message);
}

// Stream error handling
client.streamReceiverList(
  deviceId,
  (data) => { /* handle data */ },
  (error) => {
    console.error('Stream error:', error);
    // Implement retry logic or user notification
  },
  deviceIp,
  devicePort
);
```

## Development Setup

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Configure environment variables in `.env`:
```env
POSTGRES_NAME=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start development server:
```bash
python manage.py runserver
```

## Production Deployment

Use the provided Dockerfile for containerized deployment:

```bash
docker build -t skudra-backend .
docker run -p 8000:8000 skudra-backend
```

## Technologies Used

- Django 4.2
- Django REST Framework
- PostgreSQL with PostGIS
- gRPC for real-time communication
- OAuth2 for authentication
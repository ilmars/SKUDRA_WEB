# SKUDRA WEB Project
## Project Scope

This project (SWEB) is a Django + Vue application designed for real-time sensor data collection and visualization. Key features include:

1. User Management & Authentication
  - Integrates OAuth2/TARA for secure user access
  - Role-based permissions to restrict sensor control vs. data viewing
2. Sensor Interaction & gRPC Integration
 - Receives measurement data (e.g., frequency, direction-finding, audio streams) via gRPC
 - Manages sensor states (online, busy, offline) and configurations
3. Frontend Visualization (Vue)
 - Interactive map display (Leaflet/MapLibre) for sensor locations and bearings
 - Real-time spectrum plots, data tables, and optional audio playback
4. Deployment & Scalability
 - Local development with Python virtual environment and Node-based Vue dev server
 - Production-ready Dockerfiles for each service
 - Kubernetes manifests for container orchestration and scaling

The goal is to provide a robust framework for collecting, processing, and presenting sensor data in near real-time, ensuring security, ease of deployment, and extensibility for future enhancements.
                
                                 +----------------------+
                                 |   User's Browser     |
                                 |     (Vue Frontend)   |
                                 +----------+-----------+
                                            |
                           (HTTPS / WebSockets / REST)
                                            |
                                 +----------v-----------+
                                 |   Django Backend     |
                                 | (REST API, WebSockets|
                                 |   & gRPC Server)     |
                                 +----------+-----------+
                                            |
                                   (gRPC / Private Net)
                                            |
                                 +----------v-----------+
                                 |       Sensors        |
                                 | (Collect/Send Data)  |
                                 +----------------------+

                  +-----------------+           +-----------------+
                  |   PostgreSQL   |           |      Redis      |
                  |   (Database)   |           | (Channels/Cache)|
                  +-----------------+           +-----------------+


This is a skeleton structure for a Django (backend) + Vue (frontend) application,
aiming to be deployable via Docker or Kubernetes.

## Quick Start (Local Development)

1. **Backend**:
   - `cd backend`
   - `source venv/bin/activate`
   - `python manage.py runserver 0.0.0.0:8000`
   - App runs on `http://localhost:8000`

2. **Frontend**:
   - `cd frontend`
   - `npm run dev`
   - App runs on `http://localhost:5173` or similar

3. **Docker Compose**:
   - From project root: `docker-compose build`
   - Then: `docker-compose up`
   - Backend on `localhost:8000`, frontend on `localhost:8080`

## Kubernetes Deployment
- Modify the YAML files in `k8s/` as needed (images, replicas, environment variables).
- Deploy with:
  ```shell
  kubectl apply -f k8s/
  ```
# gRPC-Web JavaScript Code Generation Setup (WSL)

This guide describes how to install dependencies, build the `protoc-gen-grpc-web` plugin using Bazel, and generate JavaScript + gRPC-Web bindings from `.proto` files.

---

## Prerequisites

### 1. Update & Install System Tools

```bash
sudo apt update
sudo apt install -y protobuf-compiler nodejs npm curl gnupg
```

### 2. Install `grpc-web` JavaScript Generator

```bash
sudo npm install -g grpc-web
```

Check your installed version:

```bash
protoc --version
```

---

## Install Bazel

```bash
curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel.gpg
sudo mv bazel.gpg /etc/apt/trusted.gpg.d/
echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
sudo apt update && sudo apt install -y bazel
```

---

## Build `protoc-gen-grpc-web` Plugin

```bash
git clone https://github.com/grpc/grpc-web.git
cd grpc-web
bazel build javascript/net/grpc/web/generator/:protoc-gen-grpc-web
```

Copy the binary to your PATH:

```bash
sudo cp bazel-bin/javascript/net/grpc/web/generator/protoc-gen-grpc-web /usr/local/bin/
sudo chmod +x /usr/local/bin/protoc-gen-grpc-web
```

Verify it's available:

```bash
which protoc-gen-grpc-web
```

---

## 📁 Project Directory Setup

Make sure your project structure looks like this:

```
your-project/
├── etc/
│   └── GrpcProtos/
│       ├── simple_mode_grpc.proto
│       ├── advanced_mode_grpc.proto
├── frontend/
│   └── src/
│       └── grpc/   # <-- Generated files go here
```

---

## 🚀 Generate gRPC-Web Code

From inside `etc/GrpcProtos`:

```bash
cd /path/to/etc/GrpcProtos

protoc -I=. simple_mode_grpc.proto \
  --js_out=import_style=commonjs:../../frontend/src/grpc \
  --grpc-web_out=import_style=commonjs,mode=grpcwebtext:../../frontend/src/grpc

protoc -I=. advanced_mode_grpc.proto \
  --js_out=import_style=commonjs:../../frontend/src/grpc \
  --grpc-web_out=import_style=commonjs,mode=grpcwebtext:../../frontend/src/grpc


protoc -I=. common.proto   --js_out=import_style=commonjs:../../frontend/src/grpc   --grpc-web_out=import_style=commonjs,mode=grpcwebtext:../../frontend/src/grpc

protoc -I=. decimal_value.proto   --js_out=import_style=commonjs:../../frontend/src/grpc   --grpc-web_out=import_style=commonjs,mode=grpcwebtext:../../frontend/src/grpc

protoc -I=. shared_architecture.proto   --js_out=import_style=commonjs:../../frontend/src/grpc   --grpc-web_out=import_style=commonjs,mode=grpcwebtext:../../frontend/src/grpc

protoc -I=. welcome.proto   --js_out=import_style=commonjs:../../frontend/src/grpc   --grpc-web_out=import_style=commonjs,mode=grpcwebtext:../../frontend/src/grpc

```


```
python -m grpc_tools.protoc -IC:'/Users/ilmarsl/Development/SKUDRA WEB/SKUDRA WEB/backend/env/Lib/site-packages/grpc_tools/_proto' -Ietc/GrpcProtos --python_out=etc/GrpcProtos --grpc_python_out=etc/GrpcProtos --descriptor_set_out=etc/envoy/proto.pb etc/GrpcProtos/advanced_mode_grpc.proto etc/GrpcProtos/common.proto etc/GrpcProtos/welcome.proto etc/GrpcProtos/simple_mode_grpc.proto etc/GrpcProtos/decimal_value.proto etc/GrpcProtos/shared_architecture.proto
```

---

## ✅ Output

The following files will be generated in:

```bash
frontend/src/grpc/
```

You can now import them in your frontend application.


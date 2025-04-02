<<<<<<< HEAD
# SWEB Project

This project allows **local development** with:
1. **Python venv** in backend/
2. **Node-based** dev in frontend/

And also provides **production** setups:
- Dockerfiles for both backend & frontend
- docker-compose.yml (optional local usage)
- K8s manifests in k8s/ (for real production environments)

---

## Local Dev Steps

### Backend (Django)
1. `cd backend`
2. `source venv/bin/activate`
3. `python manage.py runserver`
4. Visit `http://localhost:8000`

### Frontend (Vue)
1. `cd frontend`
2. `npm run dev` (or `npm run serve`, depending on the Vue version)
3. Visit `http://localhost:5173` (or whichever port is shown)

---

## Docker Compose (Optional)

1. `docker-compose build`
2. `docker-compose up`
   - `backend` -> http://localhost:8000
   - `frontend` -> http://localhost:8080

---

## Kubernetes (Production)

1. **Build & Push** your images:
   ```
   cd backend
   docker build -t myregistry/sweb-backend:latest .
   docker push myregistry/sweb-backend:latest

   cd ../frontend
   docker build -t myregistry/sweb-frontend:latest .
   docker push myregistry/sweb-frontend:latest
   ```

2. **Update** `k8s/backend-deployment.yaml` and `k8s/frontend-deployment.yaml` to use:
   ```
   image: myregistry/sweb-backend:latest
   image: myregistry/sweb-frontend:latest
   ```

3. **Apply**:
   ```
   kubectl apply -f k8s/
   ```

4. **Ingress**: For `sweb.local`, either add a hosts entry or use a real domain with an Nginx Ingress controller.

Enjoy your full local dev + production environment setup!
=======
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
>>>>>>> main

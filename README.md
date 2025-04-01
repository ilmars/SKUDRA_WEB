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

# Dockerfile (Production) for Vue
FROM node:18 as build

WORKDIR /app
COPY package*.json /app/
RUN npm install

COPY . /app
RUN npm run build

# Stage 2: Serve with an HTTP server (nginx, or something else)
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80

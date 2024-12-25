
# BioHub (Updated)
## Overview
BioHub is a platform for biosafety, biostasis management, IoT monitoring, outbreak surveillance, and incident reporting. 
This updated version includes:
- WebSocket real-time updates.
- Prometheus and Grafana monitoring integration.
- Enhanced IoT and surveillance dashboards.
- Secure APIs and caching layers.
- Dockerized deployment with CI/CD pipeline.

## Setup Instructions
1. **Backend Setup**
   - Install dependencies: `npm install`.
   - Start the server: `node app.js`.

2. **Frontend Setup**
   - Navigate to the `frontend` directory.
   - Install dependencies: `npm install`.
   - Start the development server: `npm start`.

3. **Monitoring Setup**
   - Start Prometheus: `./prometheus --config.file=prometheus.yml`.
   - Start Grafana and import dashboards.

4. **Deployment**
   - Build and run Docker containers: `docker-compose up --build`.
   - Use GitHub Actions for automated CI/CD.

Refer to the documentation for further details.

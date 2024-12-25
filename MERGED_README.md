# Merged README

## Original README Content


# BioHub

BioHub is a unified, scalable, and professional platform designed to revolutionize biosafety, biostasis management, IoT monitoring, outbreak surveillance, and incident reporting. The project aligns closely with the objectives of the **Heartland BioWorks Hub (HBW)**, fostering collaboration among academia, industry, and government stakeholders.

## Features
- **Biosafety**: Manage and monitor biosafety records, aligned with the HBW BioTrain initiative.
- **Biostasis**: Track and analyze biostasis data, supporting workforce and technical innovations.
- **IoT Monitoring**: Integrate IoT devices for real-time monitoring, addressing HBW's BioLaunch goals.
- **Outbreak Surveillance**: Record and review outbreak events to strengthen regional biotech infrastructure.
- **Incident Reporting**: Log and track incidents effectively, contributing to HBW’s broader impact goals.

## HBW Membership Alignment
This platform supports the following principles outlined in the Heartland BioWorks Membership Agreement:
1. **Collaboration**: Enables stakeholders to share data and insights, fostering innovation.
2. **Governance**: Integrates workflows compatible with HBW's management boards (Executive, Scientific, Community Equity).
3. **Training and Development**: Facilitates entry-level workforce training and project tracking as part of the BioTrain initiative.

Refer to the [Heartland BioWorks Hub Membership Agreement](./Complete_with_Docusign_HBW_Membership_Agreem.pdf) for detailed governance policies.

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js and npm (for frontend)
- Docker & Docker Compose

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rfc391/BioHub
   ```

2. Run the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Access the services:
   - Backend: [http://localhost:5000](http://localhost:5000)
   - Frontend: [http://localhost:3000](http://localhost:3000)

### Testing

Run the test suite for the backend using:
```bash
pytest test_biohub.py
```

### Deployment

- Use the provided `ci-cd-pipeline.yml` for automated deployments.
- Cloudflare integration for security and performance.

---

**Contributors**: Contributions are welcome via pull requests.


## Updated README Content


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


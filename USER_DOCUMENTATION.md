
# BioHub User Documentation

## Overview
BioHub is a comprehensive platform for advancing biotechnology and biomanufacturing. This documentation guides you through setting up, configuring, and using the platform.

---

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage Guide](#usage-guide)
5. [Troubleshooting](#troubleshooting)
6. [Contribution Guidelines](#contribution-guidelines)

---

## 1. System Requirements
- Python 3.8+
- pip
- Docker (optional for containerized deployment)
- Cloudflare account for Zero Trust integration

---

## 2. Installation
### Step 1: Clone the Repository
```bash
git clone https://github.com/rfc391/BioHub.git
cd BioHub
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 3. Configuration
### Environment Variables
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Update the following placeholders with your credentials:
   - `CLOUDFLARE_TUNNEL_ID`
   - `CLOUDFLARE_API_TOKEN`
   - `CLOUDFLARE_ACCOUNT_ID`

### Database Configuration
- Cloudflare D1 and D2 databases must be linked via `cloudflare_config.json`.

---

## 4. Usage Guide
### Starting the Application
- Run the backend server:
  ```bash
  python main.py
  ```

- Run the frontend (if using Flutter):
  ```bash
  flutter run
  ```

### Accessing the Application
- Backend: [http://localhost:8000](http://localhost:8000)
- Frontend: Default Flutter project setup

---

## 5. Troubleshooting
- **Dependency Issues**: Ensure all Python dependencies are installed (`pip install -r requirements.txt`).
- **Cloudflare Errors**: Verify your credentials in `.env` and `cloudflare_config.json`.
- **Database Connectivity**: Check D1 and D2 database configurations.

---

## 6. Contribution Guidelines
1. Fork the repository.
2. Create a branch for your feature or bugfix.
3. Submit a pull request for review.

---

For additional support, please contact the BioHub development team.

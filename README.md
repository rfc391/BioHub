
# BioHub Platform

The **BioHub Platform** is a Python-based application designed to provide robust, secure, and scalable features for managing biosafety, outbreak prediction, and user data. Built on Flask, it integrates MongoDB for data storage, Redis for caching, and leverages advanced AI/ML for analytics.

## Features

- **User Management**:
  - Register and log in with secure password hashing.
  - Role-based access control (RBAC) for admin and researcher roles.
  - Password reset functionality via email tokens.

- **Outbreak Prediction**:
  - AI/ML integration for risk assessment based on input features.

- **Secure Data Access**:
  - Role-protected endpoints with granular control.

- **Performance Enhancements**:
  - Rate limiting to prevent API misuse.
  - Redis caching for fast access to frequently used data.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/biohub.git
   cd biohub
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python biohub.py
   ```

## Deployment

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t biohub:latest .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 biohub:latest
   ```

## Testing

Run tests using Pytest:
```bash
pytest test_biohub.py
```

## API Endpoints

- **`/api/register`** - Register a new user.
- **`/api/login`** - Log in and receive role information.
- **`/api/reset-password-request`** - Request a password reset token.
- **`/api/reset-password/<token>`** - Reset the password using the token.
- **`/api/secure-data`** - Access admin-only secure data.
- **`/api/outbreak-prediction`** - AI-driven outbreak prediction.

## Technologies Used

- Flask
- MongoDB (via Flask-MongoEngine)
- Redis
- Pytest

## License

This project is licensed under the MIT License.

---

**Developed By:** Your Name  
**Contact:** your-email@example.com

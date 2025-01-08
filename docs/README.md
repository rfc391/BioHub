# BioHub Project Documentation

## Overview
The BioHub Project combines a user-friendly Flask dashboard with a robust gRPC backend to provide seamless data access and management. The system ensures real-time user data retrieval and a secure, efficient backend powered by immudb, an immutable database.

---

## Features
- **Dashboard**: A web-based interface for querying and displaying user data.
- **REST API**: Lightweight REST endpoints for frontend-backend communication.
- **gRPC Backend**: High-performance backend with scalable service architecture.
- **Secure Data Storage**: Integration with immudb for immutable and verifiable data management.

---

## Project Structure
```
BioHub_Project/
├── backend/        # Backend implementation (Flask + gRPC)
│   └── app.py      # Main application file
├── frontend/       # Frontend resources (currently integrated within Flask)
├── generated/      # Auto-generated Python files for gRPC (if applicable)
├── protos/         # Protocol buffer definitions
└── docs/           # Documentation and guides
```

---

## Installation Guide

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- immudb server (Download: [immudb.io](https://www.immudb.io/))

### Steps
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd BioHub_Project
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start immudb Server**:
   Ensure the immudb server is running on your local machine.
   ```bash
   immudb
   ```

5. **Run the Application**:
   ```bash
   python backend/app.py
   ```

6. **Access the Dashboard**:
   Open a web browser and navigate to `http://localhost:5000`.

---

## REST API Reference

### Endpoint: `/get-user`
**Method**: GET  
**Description**: Fetches user details by ID.

#### Query Parameters:
- `id` (string): The ID of the user to fetch.

#### Example Request:
```bash
curl "http://localhost:5000/get-user?id=123"
```

#### Example Response:
```json
{
  "id": "123",
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

---

## Troubleshooting

### Common Issues
1. **Flask Application Not Starting**:
   - Ensure the virtual environment is activated.
   - Check that immudb is running.

2. **gRPC Errors**:
   - Verify that the backend server is listening on port `50051`.
   - Ensure no firewall is blocking the connection.

3. **Dashboard Not Loading**:
   - Confirm that the Flask server is running on `localhost:5000`.
   - Check the browser console for errors.

---

## Contribution Guide

We welcome contributions to enhance the BioHub project. Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

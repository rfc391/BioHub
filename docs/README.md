
# BioHub

BioHub is a modern platform designed to revolutionize biosafety and monitoring. It integrates IoT sensors, gRPC communication, and a modular Flask backend for seamless operation.

## Features
- **Biosafety Monitoring**: Modular routes for biosafety, biostasis, and incidents.
- **IoT Integration**: Real-time data analysis from connected devices.
- **gRPC Support**: Efficient communication with external services.
- **SQLite Database**: Lightweight and easy-to-use database management.

## Prerequisites
- Python 3.8+
- pip

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd BioHub-main
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
1. Initialize the SQLite database (if not already set up).
2. Start the Flask application:
   ```bash
   python main.py
   ```
3. The app will be accessible at `http://127.0.0.1:5000`.

## Testing
Run tests using pytest:
```bash
pytest
```

## Contributing
Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License.

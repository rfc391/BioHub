
# Ultimate Biodefense Hub

## Overview
This comprehensive project integrates biosurveillance, biostasis technology, RODS, and IoT for professional biodefense solutions.

## Features
1. Biostasis simulations and monitoring.
2. Outbreak detection and trend analysis (RODS).
3. IoT integration for real-time sensor data.
4. Compliance with ethical and regulatory standards.

## Setup Instructions
1. Clone the repository.
2. Navigate to the backend directory, run `npm install`, and then `npm start`.
3. Navigate to the frontend directory, run `npm install`, and then `npm start`.


## RODS API Endpoints

### GET /rods/historical
Retrieves historical outbreak data.

#### Response Example
```json
{
    "message": "Historical data retrieved successfully",
    "data": [
        { "date": "2023-01-01", "cases": 50 },
        { "date": "2023-02-01", "cases": 75 },
        { "date": "2023-03-01", "cases": 100 }
    ]
}
```

### Test
Run the following to test the new endpoint after starting the server:
```bash
node test_api.js
```


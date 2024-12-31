
# BioHub API Documentation

## Endpoints

### Biostasis Control
- `GET /api/biostasis/metrics`
  - Returns current biostasis metrics
  - Response: `{ temperature: number, pressure: number, humidity: number }`

- `POST /api/biostasis/simulate`
  - Simulates biostasis conditions
  - Body: `{ temperature: number, duration: number }`
  - Response: `{ id: string, status: string }`

### Real-time Monitoring
- `GET /api/monitor/status`
  - Returns system status
  - Response: `{ status: string, lastUpdate: string }`

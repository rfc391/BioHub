
# BioHub API Documentation

## Base URL
`http://localhost:5000`

---

## Endpoints

### 1. Home
**GET /**
- **Description**: Returns a welcome message.
- **Response**:
```json
{
  "message": "Welcome to BioHub - Revolutionizing Biosafety and Monitoring!"
}
```

---

### 2. Member Management
**GET /members**
- **Description**: Retrieves all members.
- **Response**:
```json
[
  {"id": "1", "name": "Alice", "email": "alice@example.com", "profile_complete": true}
]
```

**POST /members**
- **Description**: Adds a new member.
- **Request Body**:
```json
{
  "id": "1",
  "name": "Alice",
  "email": "alice@example.com",
  "profile_complete": true
}
```
- **Response**:
```json
{
  "message": "Member added!",
  "data": {...}
}
```

---

### 3. Project Tracking
**GET /projects**
- **Description**: Retrieves all projects.
- **Response**:
```json
[
  {"id": "1", "title": "Project X", "description": "Description X", "status": "ongoing"}
]
```

**POST /projects**
- **Description**: Adds a new project.
- **Request Body**:
```json
{
  "id": "1",
  "title": "Project X",
  "description": "Description X",
  "status": "ongoing"
}
```
- **Response**:
```json
{
  "message": "Project added!",
  "data": {...}
}
```

---

### 4. Compliance Checker
**GET /compliance/<member_id>**
- **Description**: Checks compliance status for a member.
- **Response**:
```json
{
  "member_id": "1",
  "compliance_status": "Compliant"
}
```

---

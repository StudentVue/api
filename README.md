# StudentVue API Server

A Flask API server that provides RESTful endpoints for accessing StudentVue data.

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:
```bash
python main.py
```

The server will run on `http://localhost:5000`

## API Endpoints

All endpoints (except health check and documentation) require a POST request with authentication parameters:

```json
{
  "username": "your_username",
  "password": "your_password",
  "district_url": "https://your-district.edupoint.com"
}
```

### Available Endpoints

- `GET /` - API documentation
- `GET /health` - Health check
- `POST /student_info` - Get student information
- `POST /school_info` - Get school information
- `POST /attendance` - Get attendance records
- `POST /calendar` - Get assignments/events calendar
- `POST /class_notes` - Get class notes
- `POST /gradebook` - Get gradebook
  - Optional parameter: `report_period` (integer)
- `POST /schedule` - Get schedule
  - Optional parameter: `term_index` (integer)
- `POST /messages` - Get messages
- `POST /documents` - List available documents
- `POST /document` - Get specific document
  - Required parameter: `document_guid` (string)
- `POST /report_cards` - List report cards
- `POST /report_card` - Get specific report card
  - Required parameter: `document_guid` (string)

## Example Usage

### Get Student Information
```bash
curl -X POST http://localhost:5000/student_info \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password",
    "district_url": "https://your-district.edupoint.com"
  }'
```

### Get Gradebook for Specific Report Period
```bash
curl -X POST http://localhost:5000/gradebook \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password", 
    "district_url": "https://your-district.edupoint.com",
    "report_period": 1
  }'
```

### Get Specific Document
```bash
curl -X POST http://localhost:5000/document \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password",
    "district_url": "https://your-district.edupoint.com",
    "document_guid": "115E2C36-DBFA-4107-AA81-979541E270A9"
  }'
```

## Response Format

All successful responses return JSON in this format:
```json
{
  "success": true,
  "data": {
    // StudentVue data here
  }
}
```

Error responses:
```json
{
  "error": "Error message",
  "traceback": "Detailed error traceback"
}
```

## Security Note

This API does not implement authentication or rate limiting. In a production environment, you should:
- Add proper authentication/authorization
- Implement rate limiting
- Use HTTPS
- Validate and sanitize all input
- Add logging and monitoring
- Consider caching to reduce load on StudentVue servers

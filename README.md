# api

APIVUE is a Flask REST API Server to fetch data from StudentVue for accessing data. It's powered by the [StudentVue.py](https://github.com/StudentVue/StudentVue.py).

There is no hosted version (at the moment) but I am working on getting one up soon.

### Running Locally
To run locally, install the requirements using
```
pip install -r requirements.txt
```

Then start the server
```
python main.py
```
This will run the server on port 3000.

### Endpoints

`GET /` - API documentation

`GET /health` - Health check

`POST /student_info` - Get student information

`POST /school_info` - Get school information

`POST /attendance` - Get attendance records

`POST /calendar` - Get assignments/events calendar

`POST /class_notes` - Get class notes

`POST /gradebook` - Get gradebook (optional param: report_period as int)

`POST /schedule` - Get schedule (optional param: term_index as int)

`POST /messages` - Get messages

`POST /documents` - List available documents

`POST /document` - Get specific document (param: document_guid as str)

`POST /report_cards` - List report cards

`POST /report_card` - Get specific report card (param: document_guid as str)

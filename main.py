from flask import Flask, request, jsonify
from studentvue import StudentVue
import traceback

app = Flask(__name__)

def create_studentvue_client(username, password, district_url):
    # creates studentvue client with creds
    try:
        return StudentVue(username, password, district_url)
    except Exception as e:
        raise Exception(f"Cannot authenticate with StudentVue, error: {str(e)}")

def validate_auth_params(data):
    required_params = ['username', 'password', 'district_url']
    missing_params = [param for param in required_params if param not in data]
    
    if missing_params:
        return False, f"Missing required parameters! Missing: {', '.join(missing_params)}"
    return True, None

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "success! APIVUE is running successfully"})

@app.route('/student_info', methods=['POST'])
def get_student_info():
    try:
        data = request.get_json()
        is_valid, error_msg = validate_auth_params(data)
        
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        sv = create_studentvue_client(data['username'], data['password'], data['district_url'])
        student_info = sv.get_student_info()
        
        return jsonify({"success": True, "data": student_info})
    
    except Exception as e:
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

@app.route('/school_info', methods=['POST'])
def get_school_info():
    try:
        data = request.get_json()
        is_valid, error_msg = validate_auth_params(data)
        
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        sv = create_studentvue_client(data['username'], data['password'], data['district_url'])
        school_info = sv.get_school_info()
        
        return jsonify({"success": True, "data": school_info})
    
    except Exception as e:
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

@app.route('/attendance', methods=['POST'])
def get_attendance():
    try:
        data = request.get_json()
        is_valid, error_msg = validate_auth_params(data)
        
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        sv = create_studentvue_client(data['username'], data['password'], data['district_url'])
        attendance = sv.get_attendance()
        
        return jsonify({"success": True, "data": attendance})
    
    except Exception as e:
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

@app.route('/calendar', methods=['POST'])
def get_calendar():
    try:
        data = request.get_json()
        is_valid, error_msg = validate_auth_params(data)
        
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        sv = create_studentvue_client(data['username'], data['password'], data['district_url'])
        calendar = sv.get_calendar()
        
        return jsonify({"success": True, "data": calendar})
    
    except Exception as e:
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

@app.route('/class_notes', methods=['POST'])
def get_class_notes():
    try:
        data = request.get_json()
        is_valid, error_msg = validate_auth_params(data)
        
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        sv = create_studentvue_client(data['username'], data['password'], data['district_url'])
        class_notes = sv.get_class_notes()
        
        return jsonify({"success": True, "data": class_notes})
    
    except Exception as e:
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

@app.route('/gradebook', methods=['POST'])
def get_gradebook():
    """Get student's gradebook"""
    try:
        data = request.get_json()
        is_valid, error_msg = validate_auth_params(data)
        
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        report_period = data.get('report_period', 0)
        
        sv = create_studentvue_client(data['username'], data['password'], data['district_url'])
        gradebook = sv.get_gradebook(report_period)
        
        return jsonify({"success": True, "data": gradebook})
    
    except Exception as e:
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

@app.route('/schedule', methods=['POST'])
def get_schedule():
    try:
        data = request.get_json()
        is_valid, error_msg = validate_auth_params(data)
        
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        term_index = data.get('term_index', 0)
        
        sv = create_studentvue_client(data['username'], data['password'], data['district_url'])
        schedule = sv.get_schedule(term_index)
        
        return jsonify({"success": True, "data": schedule})
    
    except Exception as e:
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

@app.route('/messages', methods=['POST'])
def get_messages():
    try:
        data = request.get_json()
        is_valid, error_msg = validate_auth_params(data)
        
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        sv = create_studentvue_client(data['username'], data['password'], data['district_url'])
        messages = sv.get_messages()
        
        return jsonify({"success": True, "data": messages})
    
    except Exception as e:
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

@app.route('/documents', methods=['POST'])
def list_documents():
    try:
        data = request.get_json()
        is_valid, error_msg = validate_auth_params(data)
        
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        sv = create_studentvue_client(data['username'], data['password'], data['district_url'])
        documents = sv.list_documents()
        
        return jsonify({"success": True, "data": documents})
    
    except Exception as e:
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

@app.route('/document', methods=['POST'])
def get_document():
    try:
        data = request.get_json()
        is_valid, error_msg = validate_auth_params(data)
        
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        if 'document_guid' not in data:
            return jsonify({"error": "Missing required parameter: document_guid"}), 400
        
        sv = create_studentvue_client(data['username'], data['password'], data['district_url'])
        document = sv.get_document(data['document_guid'])
        
        return jsonify({"success": True, "data": document})
    
    except Exception as e:
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

@app.route('/report_cards', methods=['POST'])
def list_report_cards():
    try:
        data = request.get_json()
        is_valid, error_msg = validate_auth_params(data)
        
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        sv = create_studentvue_client(data['username'], data['password'], data['district_url'])
        report_cards = sv.list_report_cards()
        
        return jsonify({"success": True, "data": report_cards})
    
    except Exception as e:
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

@app.route('/report_card', methods=['POST'])
def get_report_card():
    try:
        data = request.get_json()
        is_valid, error_msg = validate_auth_params(data)
        
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        if 'document_guid' not in data:
            return jsonify({"error": "Missing required parameter: document_guid"}), 400
        
        sv = create_studentvue_client(data['username'], data['password'], data['district_url'])
        report_card = sv.get_report_card(data['document_guid'])
        
        return jsonify({"success": True, "data": report_card})
    
    except Exception as e:
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

@app.route('/', methods=['GET'])
def api_documentation():
    endpoints = {
        "health": "GET /health - Health check",
        "student_info": "POST /student_info - Get student information",
        "school_info": "POST /school_info - Get school information", 
        "attendance": "POST /attendance - Get attendance records",
        "calendar": "POST /calendar - Get assignments/events calendar",
        "class_notes": "POST /class_notes - Get class notes",
        "gradebook": "POST /gradebook - Get gradebook (optional: report_period)",
        "schedule": "POST /schedule - Get schedule (optional: term_index)",
        "messages": "POST /messages - Get messages",
        "documents": "POST /documents - List documents",
        "document": "POST /document - Get specific document (requires: document_guid)",
        "report_cards": "POST /report_cards - List report cards",
        "report_card": "POST /report_card - Get specific report card (requires: document_guid)"
    }
    
    return jsonify({
        "message": "APIVUE - StudentVue REST API",
        "endpoints": endpoints,
        "required_params": {
            "username": "Student's username",
            "password": "Student's password", 
            "district_url": "District domain URL"
        },
        "example_request": {
            "username": "your_username",
            "password": "your_password",
            "district_url": "https://district.edupoint.com"
        },
        "info": "This API is under Apache License 2.0 and is provided as-is. Use at your own risk. Made by @aramshiva on github. The code is opensource at https://github.com/aramshiva/APIVUE. Thanks for using APIVUE!",
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
'''
Flask Application
'''
from flask import Flask, jsonify, request
from models import Experience, Education, Skill
from utils import validate_index

app = Flask(__name__)

data = {
    "experience": [
        Experience("Software Developer",
                   "A Cool Company",
                   "October 2022",
                   "Present",
                   "Writing Python Code",
                   "example-logo.png")
    ],
    "education": [
        Education("Computer Science",
                  "University of Tech",
                  "September 2019",
                  "July 2022",
                  "80%",
                  "example-logo.png")
    ],
    "skill": [
        Skill("Python",
              "1-2 Years",
              "example-logo.png")
    ]
}


@app.route('/test')
def hello_world():
    '''
    Returns a JSON test message
    '''
    return jsonify({"message": "Hello, World!"})


@app.route('/resume/experience', methods=['GET', 'POST'])
def experience():
    '''
    Handle experience requests
    '''
    if request.method == 'GET':
        return jsonify()

    if request.method == 'POST':
        request_data = request.get_json()
        experience_data = Experience(**request_data)
        data["experience"].append(experience_data)
        index = len(data["experience"]) - 1
        return jsonify({"id": index})

    return jsonify({})

@app.route('/resume/education', methods=['GET', 'POST', 'PUT'])
def education():
    '''
    Handles education requests
    '''
    if request.method == 'GET':
        index = request.args.get('index')
        if index is not None and index.isdigit():
            index = int(index)
            if 0 <= index < len(data["education"]):
                return jsonify(data["education"][index])
            return jsonify({"error": "Education entry not found"}), 404
        return jsonify(data["education"])

    if request.method == 'POST':
        new_education_data = request.get_json()
        new_education = Education(**new_education_data)
        data["education"].append(new_education)
        new_education_index = len(data["education"]) - 1
        return jsonify({"id": new_education_index})
    
    if request.method == 'PUT':
        update_data = request.get_json()
        index = update_data.get("id")
        if index is not None and 0 <= int(index) < len(data["education"]):
            del update_data["id"]
            updated_education = Education(**update_data)
            data["education"][int(index)] = updated_education
            return jsonify(data['education'][index])

    return jsonify({})

@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

@app.route('/resume/education/<id>', methods=['DELETE'])
def specific_education(education_id):
    '''
    Handles specific Education requests
    '''
    if not validate_index(education_id, len(data["skill"])):
        return jsonify({"error": f"Education entry {education_id} not found"}), 404
    if request.method == 'DELETE':
        index = int(education_id)
        data["skill"] = data["skill"][:index][index+1:]
        return jsonify({"inf0": "Education entry {id} has been deleted"}), 204
    return jsonify({})

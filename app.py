'''
Flask Application
'''
from flask import Flask, jsonify, request
from models import Experience, Education, Skill

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
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

@app.route('/resume/education', methods=['GET', 'POST'])
def education():
    '''
    Handles education requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})


@app.route('/resume/skill', methods=['GET', 'POST', 'PUT'])
def skill():
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        skills_data = data["skill"]
        return jsonify(skills_data)

    if request.method == 'POST':
        return jsonify({})

    if request.method == 'PUT':
        skill_data = request.get_json()
        skill_id = skill_data.get("id")

        if skill_id is not None and skill_id >= 0 and skill_id < len(data["skill"]):
            data["skill"][skill_id] = Skill(
                skill_data.get("name"),
                skill_data.get("proficiency"),
                skill_data.get("logo")
            )
            return jsonify(data['skill'][skill_id])

        return jsonify({"error": "Invalid Skill ID"}), 400

    return jsonify({})
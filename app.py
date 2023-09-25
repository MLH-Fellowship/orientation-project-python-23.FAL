'''
Title: Resume Flask Application
Author: Your Name
Date: September 20, 2023
Description: This is a Flask application for a resume API.
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
    Route: /test
    Method: GET
    Description: Returns a JSON test message.
    '''
    return jsonify({"message": "Hello, World!"})

@app.route('/resume/experience', methods=['GET', 'POST'])
def experience():
    '''
    Route: /resume/experience
    Methods: GET, POST
    Description: Handles experience requests.
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

@app.route('/resume/education', methods=['GET', 'POST'])
def education():
    '''
    Route: /resume/education
    Methods: GET, POST
    Description: Handles education requests.
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Route: /resume/skill
    Methods: GET, POST
    Description: Handles Skill requests.
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

@app.route('/resume/reorder', methods=['POST'])
def reorder_sections():
    '''
    Route: /resume/reorder
    Method: POST
    Description: Implements the logic to reorder sections.
    '''
    # Implement the logic to reorder sections here
    return jsonify({"message": "Sections Reordered"})

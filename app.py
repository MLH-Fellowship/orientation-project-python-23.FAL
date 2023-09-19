'''
Flask Application
'''
from flask import Flask, jsonify, request
from models import Experience, Education, Skill, Contact

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
    ], 
    "contact": [
        Contact("John Doe",
                "+447123456789",
                "johndoe@gmail.com")
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

@app.route('/resume/contact', methods=['GET', 'POST'])
def contact():
    '''
    Handles Contact requests
    '''
    if request.method == 'GET':
        return {"contact": data["contact"]}

    if request.method == 'POST':
        api_data = request.get_json()

        
    if api_data is not None:
        name = api_data.get("name")
        phone = api_data.get("phone")
        email = api_data.get("email")

        # Handle phone number
        if not phone.startswith("+"):
            phone = "+" + phone
        
        contact = Contact(name, phone, email)
        data["contact"].append(contact)

    return jsonify(
        {"Contact Added": contact}
    )    

@app.route('/resume/contact/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    '''
    Update a contact
    '''
    api_data = request.get_json()

    if api_data is not None:
        name = api_data.get("name")
        phone = api_data.get("phone")
        email = api_data.get("email")

        contact_list = data["contact"]
        contact = [c for c in contact_list if c.id == contact_id][0]

        # Update the contact
        contact.name = name
        contact.phone = phone
        contact.email = email

    return jsonify(
        {"Contact Updated": contact}
    )

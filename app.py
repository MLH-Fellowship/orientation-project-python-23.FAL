'''
Flask Application
'''
from flask import Flask, jsonify, request
from models import Experience, Education, Skill, User

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
    "user": [
        User("John Doe",
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

@app.route('/resume/user', methods=['GET', 'POST'])
def user():
    '''
    Handles user requests
    '''
    if request.method == 'GET':
        return {"user": data["user"]}

    if request.method == 'POST':
        api_data = request.get_json()

        
    if api_data is not None:
        name = api_data.get("name")
        phone = api_data.get("phone")
        email = api_data.get("email")

        # Handle phone number
        if not phone.startswith("+"):
            phone = "+" + phone
        
        user = User(name, phone, email)
        data["user"].append(user)

    return jsonify(
        {"A person Added": user}
    )    

@app.route('/resume/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    '''
    Update a contact
    '''
    api_data = request.get_json()

    if api_data is not None:
        name = api_data.get("name")
        phone = api_data.get("phone")
        email = api_data.get("email")

        user_list = data["user"]
        user = [user for user in user_list if user.id == user_id][0]

        # Update the contact
        user.name = name
        user.phone = phone
        user.email = email

    return jsonify(
        {"Person Info Updated": user}
    )

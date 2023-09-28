"""
Flask Application
"""
# pylint: disable=too-many-return-statements
from typing import Any
from flask import Flask, jsonify, request
import openai as oai
from models import Experience, Education, Skill
from utils import validate_index, OpenAIServiceError

app = Flask(__name__)

data = {
    "experience": [
        Experience(
            "Software Developer",
            "A Cool Company",
            "October 2022",
            "Present",
            "Writing Python Code",
            "example-logo.png",
        )
    ],
    "education": [
        Education(
            "Computer Science",
            "University of Tech",
            "September 2019",
            "July 2022",
            "80%",
            "example-logo.png",
        )
    ],
    "skill": [Skill("Python", "1-2 Years", "example-logo.png")],
}


@app.route("/test")
def hello_world():
    """
    Returns a JSON test message
    """
    return jsonify({"message": "Hello, World!"})


@app.route("/resume/experience", methods=["GET", "POST", "DELETE"])
def experience():
    """
    Handle experience requests
    """
    if request.method == "GET":
        index = request.args.get("index")
        if index and index.isdigit():
            index = int(index)
            if index in range(len(data["experience"])):
                return jsonify(data["experience"][index])

            return jsonify({"error": f"No Experience entry with index {index}"}), 404

        return jsonify(data["experience"])

    if request.method == "POST":
        request_data = request.get_json()
        experience_data = Experience(**request_data)
        data["experience"].append(experience_data)
        index = len(data["experience"]) - 1
        return jsonify({"id": index})

    if request.method == "DELETE":
        index = request.args.get("index")
        if index and index.isdigit():
            index = int(index)
            if index in range(len(data["experience"])):
                removed_entry = data["experience"].pop(index)
                return (
                    jsonify(
                        {
                            "message": f"Experience entry with index {index} deleted successfully",
                            "data": removed_entry,
                        }
                    ),
                    200,
                )

            return jsonify({"error": f"No Experience entry with index {index}"}), 404

        return jsonify({"error": "No index provided"}), 404

    return jsonify({})


@app.route("/resume/education", methods=["GET", "POST"])
def education():
    """
    Handles education requests
    """
    if request.method == "GET":
        index = request.args.get("index")
        if index is not None and index.isdigit():
            index = int(index)
            if 0 <= index < len(data["education"]):
                return jsonify(data["education"][index])
            return jsonify({"error": "Education entry not found"}), 404
        return jsonify(data["education"])

    if request.method == "POST":
        new_education_data = request.get_json()
        new_education = Education(**new_education_data)
        data["education"].append(new_education)
        new_education_index = len(data["education"]) - 1
        return jsonify({"id": new_education_index})
    return jsonify({})


@app.route("/resume/skill", methods=["GET", "POST", "DELETE"])
def skill():
    """
    Handles Skill requests
    """
    if request.method == "GET":
        return jsonify({})

    if request.method == "POST":
        return jsonify({})

    if request.method == "DELETE":
        index = request.args.get("index", type=int)
        if index is not None and 0 <= index < len(data["skill"]):
            deleted_skill = data["skill"].pop(index)
            return jsonify(
                {"message": f"Skill '{deleted_skill.name}' deleted successfully"}
            )

    return jsonify({})


@app.route("/resume/education/<id>", methods=["DELETE"])
def specific_education(education_id):
    """
    Handles specific Education requests
    """
    if not validate_index(education_id, len(data["skill"])):
        return jsonify({"error": f"Education entry {education_id} not found"}), 404
    if request.method == "DELETE":
        index = int(education_id)
        data["skill"] = data["skill"][:index][index + 1 :]
        return jsonify({"inf0": "Education entry {id} has been deleted"}), 204
    return jsonify({})


@app.route('/resume/gpt_description', methods=['POST'])
async def chat_gpt_description():
    '''
    Uses openAI API to generate descriptions for the exeprience field.
    It creates a prompt using the experience data and sends it to the API.
    '''
    if request.method == 'POST':
        index = request.args.get('index')
        api_key = request.form.get('api_key')
        if index is not None and index.isdigit():
            index = int(index)
            if 0 <= index < len(data["experience"]):
                experience_data = data["experience"][index]
                prompt = """
                I need you to help me write a description for my experience section
                on my resume. Respond with the description and nothing else, do not
                include a greeting or any other text in your response. Use this 
                information to help you write a description for the following entry:
                """
                prompt += f"\nTitle: {experience_data.title}\n"
                prompt += f"Company: {experience_data.company}\n"
                prompt += f"Start Date: {experience_data.start_date}\n"
                prompt += f"End Date: {experience_data.end_date}\n"
                response = await _send_chat_request(prompt, api_key)
                response = response.choices[0].message.content
                return jsonify({"id": index, "response": response})
            return jsonify({"error": "Experience entry not found"}), 404
        return jsonify({"error": "Invalid index"}), 400


async def _send_chat_request(prompt, api_key):
    '''
    Helper function that handles the chat request to the OpenAI API.
    '''
    response = ""
    oai.api_key = api_key
    formatted_message = [
            {"role": "user", "content": prompt}
    ]
    try:
        response: Any = await oai.ChatCompletion.acreate(
            model= "gpt-3.5-turbo",
            messages= formatted_message,
        )
    except Exception as exception:
        raise OpenAIServiceError(
            f"OpenAI service failed to complete the chat: {exception}"
        ) from exception
    return response


@app.route('/resume/approve', methods=['POST'])
def approve_description():
    '''
    Gets user approval to use the chat gpt generated description.
    '''
    index = request.form.get('index')
    description = request.form.get('description')
    data["experience"][index].description = description

    return jsonify({"status": "approved"})

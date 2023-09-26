"""
Flask Application
"""
# pylint: disable=too-many-return-statements
from flask import Flask, jsonify, request
from models import Experience, Education, Skill
from utils import validate_index

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
        experience_properties = ["title","company","start_date","end_date","description","logo"]
        # Checks if an experience property is missing in request_data
        for prop in experience_properties:
            if prop not in request_data:
                return jsonify({"error":"Missing one or more input fields"}), 400
        # Removes any unnecessary properties in request_data
        for key in list(request_data.keys()):
            if key not in experience_properties:
                del request_data[key]

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

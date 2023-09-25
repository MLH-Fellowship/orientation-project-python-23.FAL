"""
Tests in Pytest
"""
from app import app


def test_client():
    """
    Makes a request and checks the message received is the same
    """
    response = app.test_client().get("/test")
    assert response.status_code == 200
    assert response.json["message"] == "Hello, World!"


def test_experience():
    """
    Add a new experience and then get all experiences.

    Check that it returns the new experience in that list
    """
    example_experience = {
        "title": "Software Developer",
        "company": "A Cooler Company",
        "start_date": "October 2022",
        "end_date": "Present",
        "description": "Writing JavaScript Code",
        "logo": "example-logo.png",
    }

    item_id = (
        app.test_client().post("/resume/experience", json=example_experience).json["id"]
    )
    response = app.test_client().get("/resume/experience")
    assert response.json[item_id] == example_experience

    delete_response = app.test_client().delete(f"/resume/education?index={item_id}")
    assert delete_response.status_code == 200

    response_after_deletion = app.test_client().get("/resume/education")
    assert item_id not in response_after_deletion.json


def test_education():
    """
    Add a new education and then get all educations.

    Check that it returns the new education in that list
    """
    example_education = {
        "course": "Engineering",
        "school": "NYU",
        "start_date": "October 2022",
        "end_date": "August 2024",
        "grade": "86%",
        "logo": "example-logo.png",
    }
    item_id = (
        app.test_client().post("/resume/education", json=example_education).json["id"]
    )

    response = app.test_client().get("/resume/education")
    assert response.json[item_id] == example_education

    response =  app.test_client().delete('/resume/education/1')
    assert response.status_code ==  204

    response = app.test_client().delete('/resume/education/100')
    assert response.status_code == 404


def test_skill():
    """
    Add a new skill and then get all skills.

    Check that it returns the new skill in that list
    """
    example_skill = {
        "name": "JavaScript",
        "proficiency": "2-4 years",
        "logo": "example-logo.png",
    }

    item_id = app.test_client().post("/resume/skill", json=example_skill).json["id"]

    response = app.test_client().get("/resume/skill")
    assert response.json[item_id] == example_skill

    response = app.test_client().get('/resume/skill/1')
    assert response.status_code == 200

    response = app.test_client().get('/resume/skill/1000')
    assert response.status_code == 404

def test_delete_skill():
    '''
    Delete a skill and then check that it's no longer in the list
    '''

    example_skill = {
        "skill": ["Python", "Javascript", "C++"]
    }

    item_id = app.test_client().post('/resume/skill', json=example_skill).json['id']

    index_to_delete = 0
    skill_name = example_skill["skill"][index_to_delete]
    response = app.test_client().delete(f'/resume/skill?index={index_to_delete}')
    assert response.json[item_id] == example_skill

    assert response.status_code == 200  # Check for a successful delete
    assert "message" in response.json
    assert response.json["message"] == f"Skill '{skill_name}' deleted successfully"

    # Check that the deleted skill is no longer in the list
    response = app.test_client().get('/resume/skill')
    assert skill_name not in response.json

def test_update_experience():
    '''
    Update an existing experience and check that it has been updated successfully
    '''
    # Update the experience
    updated_experience = {
        "id": 0,
        "title": "Updated Title",
        "company": "Updated Company",
        "start_date": "Updated Start Date",
        "end_date": "Updated End Date",
        "description": "Updated Description",
        "logo": "updated-logo.png"
    }

    response = app.test_client().put('/resume/experience', json=updated_experience)

    assert response.status_code == 200
    assert response.json["title"] == updated_experience["title"]

    # Check if the skill has been updated in the list
    get_response = app.test_client().get('/resume/experience')
    updated_experience_list = get_response.json

    experience_id = updated_experience["id"]
    del updated_experience["id"]

    assert len(updated_experience_list) == 1
    assert updated_experience_list[experience_id] == updated_experience

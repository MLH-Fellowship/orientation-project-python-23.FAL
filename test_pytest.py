'''
Tests in Pytest
'''
from app import app


def test_client():
    '''
    Makes a request and checks the message received is the same
    '''
    response = app.test_client().get('/test')
    assert response.status_code == 200
    assert response.json['message'] == "Hello, World!"


def test_experience():
    '''
    Add a new experience and then get all experiences. 
    
    Check that it returns the new experience in that list
    '''
    example_experience = {
        "title": "Software Developer",
        "company": "A Cooler Company",
        "start_date": "October 2022",
        "end_date": "Present",
        "description": "Writing JavaScript Code",
        "logo": "example-logo.png"
    }

    item_id = app.test_client().post('/resume/experience',
                                     json=example_experience).json['id']
    response = app.test_client().get('/resume/experience')
    assert response.json[item_id] == example_experience


def test_education():
    '''
    Add a new education and then get all educations. 
    
    Check that it returns the new education in that list
    '''
    example_education = {
        "course": "Engineering",
        "school": "NYU",
        "start_date": "October 2022",
        "end_date": "August 2024",
        "grade": "86%",
        "logo": "example-logo.png"
    }
    item_id = app.test_client().post('/resume/education',
                                     json=example_education).json['id']

    response = app.test_client().get('/resume/education')
    assert response.json[item_id] == example_education

    response =  app.test_client().delete('/resume/education/1')
    assert response.status_code ==  204

    response = app.test_client().delete('/resume/education/100')
    assert response.status_code == 404


def test_skill():
    '''
    Add a new skill and then get all skills. 
    
    Check that it returns the new skill in that list
    '''
    example_skill = {
        "name": "JavaScript",
        "proficiency": "2-4 years",
        "logo": "example-logo.png"
    }

    item_id = app.test_client().post('/resume/skill',
                                     json=example_skill).json['id']

    response = app.test_client().get('/resume/skill')
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

def test_update_skill():
    '''
    Update an existing skill by passing the ID in the JSON request
    '''

    updated_skill = {
        "id": 0,
        "name": "Updated Skill",
        "proficiency": "5-7 years",
        "logo": "example-logo.png"
    }

    # Perform the PUT request to update the skill without passing ID in the URL
    response = app.test_client().put('/resume/skill', json=updated_skill)

    assert response.status_code == 200
    assert response.json["name"] == updated_skill["name"]

    # Check if the skill has been updated in the list
    get_response = app.test_client().get('/resume/skill')
    updated_skill_list = get_response.json

    skill_id = updated_skill["id"]
    del updated_skill["id"]

    assert len(updated_skill_list) == 1
    assert updated_skill_list[skill_id] == updated_skill

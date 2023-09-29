# pylint: disable=R0913

'''
Title: Resume API Models
Author: Your Name
Date: September 20, 2023
Description: This module contains data models for the Resume API.
'''

from dataclasses import dataclass
from typing import List


@dataclass
class PersonalInfo:
    '''
    User details
    '''
    first_name: str
    last_name: str
    middle_name: str

@dataclass
class Experience:
    '''
    Class: Experience
    Description: Represents an experience entry in a resume.
    '''
    title: str
    company: str
    start_date: str
    end_date: str
    description: str
    logo: str
    order: int  # Adding the 'order' attribute. It defines the position of the Experience class and can be of use for sorting the order of experience in a resume in ascending order

@dataclass
class Education:
    '''
    Class: Education
    Description: Represents an education entry in a resume.
    '''
    course: str
    school: str
    start_date: str
    end_date: str
    grade: str
    logo: str
    order: int  # Adding the 'order' attribute. It defines the position of the Education class and can be of use for sorting the order of experience in a resume.

@dataclass
class Skill:
    '''
    Class: Skill
    Description: Represents a skill entry in a resume.
    '''
    name: str
    proficiency: str
    logo: str

    order: int  # Adding the 'order' attribute. It defines the position of the skill class and can be of use for sorting the order of experience in a resume.

@dataclass
class Project:
    '''
    Project class
    '''
    name: str
    languages: List[str]
    description: str
    link: str
    order: int  # Adding the 'order' attribute. It defines the position of the project class and can be of use for sorting the order of experience in a resume.

# pylint: disable=R0913

'''
Title: Resume API Models
Author: Your Name
Date: September 20, 2023
Description: This module contains data models for the Resume API.
'''

from dataclasses import dataclass

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
    order: int  # Adding the 'order' attribute to help set the order of the class

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
    order: int  # Adding the 'order' attribute to help set the order of the class

@dataclass
class Skill:
    '''
    Class: Skill
    Description: Represents a skill entry in a resume.
    '''
    name: str
    proficiency: str
    logo: str
    order: int  # Adding the 'order' attribute to help set the order of the class

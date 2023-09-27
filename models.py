# pylint: disable=R0913

'''
Models for the Resume API. Each class is related to
'''

from dataclasses import dataclass
from typing import List

@dataclass
class Bio:
    '''
    Bio Class
    '''
    about: str

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
    Experience Class
    '''
    title: str
    company: str
    start_date: str
    end_date: str
    description: str
    logo: str


@dataclass
class Education:
    '''
    Education Class
    '''
    course: str
    school: str
    start_date: str
    end_date: str
    grade: str
    logo: str


@dataclass
class Skill:
    '''
    Skill Class
    '''
    name: str
    proficiency: str
    logo: str


@dataclass
class Project:
    '''
    Project class
    '''
    name: str
    languages: List[str]
    description: str
    link: str

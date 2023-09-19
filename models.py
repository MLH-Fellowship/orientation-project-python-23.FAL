# pylint: disable=R0913

'''
Models for the Resume API. Each class is related to
'''

from dataclasses import dataclass


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
class User:
    '''
    Contact Class
    '''
    id: int
    name: str
    phone: str
    email: str

    id_counter = 1

    def __init__(self, name, phone, email):
        self.id = User.id_counter
        User.id_counter += 1
        self.name = name
        self.phone = phone
        self.email = email
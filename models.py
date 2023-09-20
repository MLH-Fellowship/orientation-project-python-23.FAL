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
    order: int  # Adding the 'order' attribute to help setting the order of the class

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
    order: int  # Adding the 'order' attribute to help setting the order of the class

@dataclass
class Skill:
    '''
    Skill Class
    '''
    name: str
    proficiency: str
    logo: str
    order: int  # Adding the 'order' attribute to help setting the order of the class

class Contact:
    def __init__(self, name, age, address, phone_number, email):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    # ... and so on for all the other attributes

class Job:
    def __init__(self, employer, job_title, job_description, job_start_date, job_end_date):
        self.employer = employer
        self.job_title = job_title
        self.job_description = job_description
        self.job_start_date = job_start_date
        self.job_end_date = job_end_date

class Education:
    def __init__(self, education_level, school_name, major, minor, degree_type, degree_start_date, degree_end_date):
        self.education_level = education_level
        self.school_name = school_name
        self.major = major
        self.minor = minor
        self.degree_type = degree_type
        self.degree_start_date = degree_start_date
        self.degree_end_date = degree_end_date

class Certification:
    def __init__(self, certification_name, certification_start_date, certification_end_date, certification_description):
        self.certification_name = certification_name
        self.certification_start_date = certification_start_date
        self.certification_end_date = certification_end_date
        self.certification_description = certification_description

class Skill:
    def __init__(self, skill_name):
        self.skill_name = skill_name

class Person:
    def __init__(self, contact:Contact, job, education, certification, skills: list[Skill]):
        self.contact = contact
        self.job = job
        self.education = education
        self.certification = certification
        self.skills = skills

Person()
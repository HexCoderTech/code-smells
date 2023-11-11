class Person:
    def __init__(self, name, age, address, phone_number, email, occupation, employer, job_title, job_description, job_start_date, job_end_date, education_level, school_name, major, minor, degree_type, degree_start_date, degree_end_date, certification_name, certification_start_date, certification_end_date, certification_description, skill1, skill2, skill3, skill4, skill5, skill6, skill7, skill8, skill9, skill10):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.occupation = occupation
        self.employer = employer
        self.job_title = job_title
        self.job_description = job_description
        self.job_start_date = job_start_date
        self.job_end_date = job_end_date
        self.education_level = education_level
        self.school_name = school_name
        self.major = major
        self.minor = minor
        self.degree_type = degree_type
        self.degree_start_date = degree_start_date
        self.degree_end_date = degree_end_date
        self.certification_name = certification_name
        self.certification_start_date = certification_start_date
        self.certification_end_date = certification_end_date
        self.certification_description = certification_description
        self.skill1 = skill1
        self.skill2 = skill2
        self.skill3 = skill3
        self.skill4 = skill4
        self.skill5 = skill5
        self.skill6 = skill6
        self.skill7 = skill7
        self.skill8 = skill8
        self.skill9 = skill9
        self.skill10 = skill10

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    # ... and so on for all the other attributes

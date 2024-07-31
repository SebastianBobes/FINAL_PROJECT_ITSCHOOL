class Member:
    def __init__(self, last_name: str ,first_name: str,
                 telephone_number: str,study_year: str,
                 college: int, middle_name: str, events: list = [] , department_id: int = None):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.telephone_number = telephone_number
        self.study_year = study_year
        self.college = college
        self.department_id = department_id
        self.events = events
        self.email = self.create_email_address()
    def create_email_address(self):
        if self.middle_name == '':
            email = f"{self.first_name.lower()}.{self.last_name.lower()}@euroavia-bucuresti.ro"
        else:
            email = f"{self.first_name.lower()}-{self.middle_name.lower()}.{self.last_name.lower()}@euroavia-bucuresti.ro"
        return email



















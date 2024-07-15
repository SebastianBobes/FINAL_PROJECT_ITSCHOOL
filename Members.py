class Member:
    def __init__(self, last_name: str ,first_name: str,
                 telephone_number: str,study_year: str,
                 college: str, middle_name: str, events: list = [] , department_id: int = None):
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

# class Heads(Member):
#     def __init__(self, last_name: str, first_name: str, telephone_number: str, study_year: str, college: str,
#                  middle_name:str, department_head_of: str = None):
#         super().__init__(last_name, first_name, middle_name, telephone_number, study_year, college)
#         self.department_head_of = department_head_of
#
#
# class Member_of_local_board(Heads):
#     def __init__(self, last_name: str, first_name: str, middle_name:str, telephone_number: str, study_year: str, college: str,
#                  position: str):
#         super().__init__(last_name, first_name,middle_name, telephone_number, study_year, college)
#         self.position = position
















class UserAlreadyExists(Exception):
    def __int__(self, message):
        self.message = "User already exists!!!!! cannot create duplicate user"

class MobileAlreadyExists(Exception):

    def __int__(self, error):
        self.error = "Mobile already exists!!!!!"



class QuestionAlreadyExists(Exception):


    def __int__(self, issue):
        self.issue = "Question Already Exists!!!!!"
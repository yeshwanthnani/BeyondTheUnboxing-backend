class UserAlreadyExists(Exception):
    def __init__(self):
        self.message = "User already exists cannot create duplicate user"


class UserDoesNotExist(Exception):
    def __init__(self):
        self.message = "Sorry! User does not Exist"


class MobileAlreadyExists(Exception):
    def __init__(self):
        self.message = "Mobile already exists"


class MobileDoesNotExists(Exception):
    def __init__(self):
        self.message = "Mobile Does Not exist"


class MobileBrandDoesNotExists(Exception):
    def __init__(self):
        self.message = "Mobile Brand Does Not exist"


class QuestionAlreadyExists(Exception):
    def __init__(self):
        self.message = "Question Already Exists"


class QuestionDoesNotExists(Exception):
    def __init__(self):
        self.message = "Question Does Not Exist"


class MobileBrandUnknown(Exception):

    def __init__(self):
        self.message = "Mobile Brand Unknown"


class Failed(Exception):
    def __init__(self):
        self.message = "Failed"

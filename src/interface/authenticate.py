from dataclasses import dataclass

@dataclass
class authenticateParamsInterface:
    def __init__(self):
        self.successRedirect = str
        self.failureRedirect = str
AuthenticateParams = authenticateParamsInterface()


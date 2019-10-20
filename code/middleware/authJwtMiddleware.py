import jwt

class authJwtMiddleware():
    def __init__(self, next, token):
        self.next = next
        self.token = token

    def handle(self):
        if(self.token == "rudi"):
            return self.next
        else:
            return "Token empty or not valid !!!"
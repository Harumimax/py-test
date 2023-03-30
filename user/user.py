class User():
    def __init__(self, login, password, mode="user"):
        self.login = login
        self.hash = password
        self.password = password
        self.mode = mode

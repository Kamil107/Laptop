class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def information(self):
        print(f"Username: {self.username}, password: {self.password}")


u1 = User("Kamil", "Haslo")
u1.information()
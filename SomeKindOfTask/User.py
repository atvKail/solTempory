class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    
    def __repr__(self):
        return f"User(nickname='{self.nickname}', age={self.age})"
    
    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password

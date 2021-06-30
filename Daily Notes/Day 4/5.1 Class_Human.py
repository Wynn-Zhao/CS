class Human:
    def __init__(self, name, gender = 'Male', age = 18, iq = 180, height = 180):
        self.name = name
        self.gender = gender
        self.age = age
        self.iq = iq
        self.height = height
        self.friends = []

    def __str__(self):
        return 'Human: ' + self.name

    def __repr__(self):
        return 'Human: ' + self.name

    def greeting(self):
        return 'Hello, my name is ' + self.name

    def add_friend(self, friend):
        self.friends.append(friend)

h = Human('Wynn')
print(h.greeting())

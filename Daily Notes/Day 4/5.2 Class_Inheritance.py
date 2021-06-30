class Animal:
    def __init__(self, weight, height, sex, color):
        self.weight = weight
        self.height = height
        self.sex = sex
        self.color = color

    def introduction(self):
        return self.weight


class Dog(Animal):
    def __init__(self, weight, height, sex, color, name):
        self.name = name
        super().__init__(weight, height, sex, color)

    def woof(self):
        return 'woof! I am ' + self.name


d = Dog('6lb', '40cm', 'Male', 'yellow', 'Doggy')
print(d.introduction())
print(d.woof())
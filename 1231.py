 class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

kitty = Student('Kitty', 85, 30)
daniel = Student('Daniel', 80, 30)

print(kitty.name)
print(daniel.name)

print(kitty.grade)
print(daniel.grade)
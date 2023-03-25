class Persone():
    def __init__(self, name="None", age=0, born_place="None", sex="Not defined", citizenship="Russian"):
        self.name = name
        self.age = age
        self.born_place = born_place
        self.sex = sex
        self.citizenship = citizenship

    def age_persone(self):
        self.age += 1

    def introduce(self):
        print("Hi! My name is %s. I'm %d years old. I was born in %s." % (self.name, self.age, self.born_place))

class Student(Persone):

    def __init__(self, name="None", age=0, born_place="None", sex="Not defined", citizenship="Russian", school="None", graduat_year=1900, average_rate=0, course="None"):
        super().__init__(name, age, born_place, sex, citizenship)
        self.school = school
        self.graduat_year = graduat_year
        self.average_rate = average_rate
        self.course = course

    def introduce_student(self):
        print("Hi! My name is %s. I'm a Student. I'm %d years old. I was born in %s. And I'm going to graduat a %s in %d. I learn on %s course." % (self.name, self.age, self.born_place, self.school, self.graduat_year, self.course))
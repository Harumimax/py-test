"""Создание класса "Студент" с атрибутами "имя", "фамилия", "курс", "средний балл".
Реализовать методы для добавления и удаления студента, изменения данных студента,
вывода информации о всех студентах, а также поиска студента по фамилии."""


# импортируем класс
class Student:
    _students = []
    def __init__(self, name, sname, course, score):
            self.name = name
            self.sname = sname
            self.course = course
            self.score = score
            #Student._students = []

    @classmethod
    def add_student(cls, student):
        cls._students.append(student)

    def change_course(self, course):
        self.course = course

    @classmethod
    def print_students(cls):
        for student in cls._students:
            print(f'{student.name} {student.sname}, course: {student.course}, score: {student.score}')

    @classmethod
    def search_student(cls, sname):
        result = "Cтудент не найден!"
        for student in cls._students:
            if student.sname == sname:
                result = f"{student.name} {student.sname}, course: {student.course}, score: {student.score}"
        print(result)


# создаем объекты студентов
student1 = Student("Иван", "Иванов", 1, 4.5)
student2 = Student("Петр", "Петров", 2, 3.7)

# добавляем студента
student3 = Student("Сергей", "Сергеев", 1, 4.0)
Student.add_student(student3)
Student.add_student(student1)


# изменяем данные студента
student1.change_course(4)

# выводим информацию о всех студентах
Student.print_students()
print("-----------------------------")

# ищем студента по фамилии
Student.search_student("Иванов")
Student.search_student("Иванова")


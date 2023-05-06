from persone.persone import Persone
from persone.persone import Student

# tast 1
tanya = Persone("Tanya", 18, "Moscow")
tanya.introduce()
tanya.age_persone()
tanya.introduce()
tanya.born_place = "Spb"
tanya.introduce()
# tast 2
tanya_student = Student(tanya.name, tanya.age, tanya.born_place, tanya.sex, tanya.citizenship, "School №5", 2025, 3.5)
tanya_student.introduce_student()
tanya_student.course = "Автоматический тестировщик"
tanya_student.age = 25
tanya_student.introduce_student()
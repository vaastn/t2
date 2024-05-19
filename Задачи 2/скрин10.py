class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.subjects = {}

    def add_subject(self, subject, grade):
        self.subjects[subject] = grade

    def remove_subject(self, subject):
        if subject in self.subjects:
            del self.subjects[subject]
        else:
            print(f"{subject} не найден в массиве")

    def calculate_average_grade(self):
        if len(self.subjects) == 0:
            print("не найдено")
            return 0

        total_grade = sum(self.subjects.values())
        return total_grade / len(self.subjects)

# проверка функциональности класса
student1 = Student("Иван", 20)
student1.add_subject("Математика", 85)
student1.add_subject("Физика", 90)
student1.add_subject("Информатика", 80)

print(f"{student1.name} средний балл: {student1.calculate_average_grade()}")

student1.remove_subject("Физика")

print(f"После удаления Физики средний балл {student1.name}: {student1.calculate_average_grade()}")

student2 = Student("Мария", 22)
student2.add_subject("Математика", 75)
student2.add_subject("Физика", 70)

print(f"{student2.name} средний балл: {student2.calculate_average_grade()}")

class Nikola:
    def __init__(self, name, age):
        self.age = age
        if name == "Николай":
            self.name = name
        else:
            self.name = f"Я не {name}, а Николай мне"

# добавляем значения
nikola1 = Nikola("Николай", 30)
nikola2 = Nikola("Максим", 25)

# вывод
print(nikola1.name, nikola1.age)
print(nikola2.name, nikola2.age)

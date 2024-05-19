class Soda:
  #класс для моделирования газированной воды

  def __init__(self, additive):
    #инициализация класса

    #Args:
      #additive: строка, описывающая добавку к лимонаду

    self.additive = additive

  def show_my_drink(self):
    #вывод информации о напитке

    if self.additive:
      return f"Газировка и ({self.additive})"
    else:
      return "Обычная газировка"

# пример использования

soda1 = Soda("Лимон")
soda2 = Soda("")

print(soda1.show_my_drink())  # Газировка и (Лимон)
print(soda2.show_my_drink())  # Обычная газировка

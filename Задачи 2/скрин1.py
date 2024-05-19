class Book:
  #Класс для представления книги.

  #Атрибуты:
    #title: Название книги.
    #author: Автор книги.

  #Методы:
    #get_title(): Возвращает название книги.
    #get_author(): Возвращает автора книги.

  def __init__(self, title, author):
    
    #конструктор класса Book

    #аргументы:
      #title: название книги
      #author: автор книги
    
    self.title = title
    self.author = author

  def get_title(self):
    #возвращает название книги
    return self.title

  def get_author(self):
    #возвращает автора книги
    return self.author

# пример использования

book1 = Book("Война и мир", "Лев Толстой")
print(f"Название книги: {book1.get_title()}")  # выведет: Название книги: Война и мир
print(f"Автор книги: {book1.get_author()}")  # Выведет: Автор книги: Лев Толстой

class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)
        print(f'Книга "{book}" добавлена в библиотеку')

    def remove_book(self, book):
        if book in self.book_list:
            self.book_list.remove(book)
            print(f'Книга "{book}" удалена из библиотеки')
        else:
            print(f'Книги "{book}" нет в библиотеке')

    def find_book_by_title(self, title):
        found_books = [book for book in self.book_list if title.lower() in book.lower()]
        if found_books:
            print(f'Найдены книги с названием "{title}": {", ".join(found_books)}')
        else:
            print(f'Книги с названием "{title}" не найдены в библиотеке')


# пример использования класса
library1 = Library()

library1.add_book("Война и мир")
library1.add_book("Преступление и наказание")
library1.add_book("Мастер и Маргарита")

library1.find_book_by_title("Мастер")
library1.find_book_by_title("Преступление")
library1.find_book_by_title("Гарри Поттер")

library1.remove_book("Мастер и Маргарита")
library1.remove_book("1984")

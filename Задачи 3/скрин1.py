def read_file(filename):
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def main():
    # создание и запись текста в файл
    try:
        with open("example.txt", 'w', encoding='UTF-8') as file:
            file.write("Это первая строка\n")
            file.write("Это вторая строка\n")
            file.write("Это третья строка")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")
    
    # чтение файла и вывод содержимого на экран
    read_file("example.txt")

if __name__ == "__main__":
    main()

import csv


# создаем CSV-файл и записываем в него данные
def create_csv(filename):
    data = [
        ["Анна", "Валерьевна", 30],
        ["Анна", "Татаринова", 25],
        ["Анна", "Лучшая", 35]
    ]
    with open(filename, 'w', newline='', encoding='UTF-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Имя", "Фамилия", "Возраст"])
        writer.writerows(data)

# функция для чтения и вывода содержимого CSV-файла
def read_csv(filename):
    with open(filename, 'r', newline='', encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(', '.join(row))

# создаем CSV-файл
create_csv("data.csv")

# читаем и выводим содержимое CSV-файла
print("Содержимое файла 'data.csv':")
read_csv("data.csv")

import os
import csv


# функция для чтения данных из CSV файла и анализа
def analyze_csv(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        user_data = [row for row in reader]
        return user_data

# функция для вывода сводной информации
def print_summary(user_data):
    # пример вывода: средний возраст пользователей
    ages = [int(user['age']) for user in user_data]
    average_age = sum(ages) / len(ages)
    print("Средний возраст пользователей:", average_age)

    # дополнительные статистики могут быть добавлены здесь

# сканирование директории "data"
data_dir = "data"
files = os.listdir(data_dir)
for file_name in files:
    if file_name.endswith('.csv'):
        file_path = os.path.join(data_dir, file_name)
        print("Анализ файла:", file_name)
        user_data = analyze_csv(file_path)
        print_summary(user_data)
        print()  # пустая строка для читаемости вывода

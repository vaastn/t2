import csv


def process_csv(file_name, column_index):
    # инициализируем переменные для подсчета суммы и количества значений в столбце
    total = 0
    count = 0
    
    try:
        with open(file_name, 'r', newline='', encoding='UTF-8') as file:
            reader = csv.reader(file)
            # пропускаем заголовок, если он есть
            next(reader)
            for row in reader:
                # проверяем, что строка имеет достаточное количество элементов
                if len(row) > column_index:
                    try:
                        # пытаемся преобразовать значение столбца в число и добавить его к общей сумме
                        total += float(row[column_index])
                        # увеличиваем счетчик значений
                        count += 1
                    except ValueError:
                        # если значение не удалось преобразовать в число, игнорируем его
                        pass
    except FileNotFoundError:
        print("Файл не найден.")
        return None
    
    # проверяем, были ли найдены какие-либо значения в столбце
    if count > 0:
        # возвращаем среднее значение
        return total / count
    else:
        print("Не удалось найти значения в указанном столбце.")
        return None

# пример использования функции
file_name = "weather.csv"
column_index = 3  # например, индекс столбца с температурой

average_temperature = process_csv(file_name, column_index)
if average_temperature is not None:
    print(f"Средняя температура: {average_temperature}")

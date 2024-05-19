import pandas as pd


def main():
    file_path = 'data.csv'
    
    try:
        # считываем данные из CSV-файла
        data = pd.read_csv(file_path)
        
        # выводим статистику по каждому столбцу
        for column in data.columns:
            print(f"Статистика для столбца '{column}':")
            print(data[column].describe())
            print("\n")
    
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print("Произошла ошибка при чтении файла:", e)

if __name__ == "__main__":
    main()

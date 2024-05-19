import pandas as pd


def merge_csv_files(output_file, *input_files):
    # чтение данных из каждого CSV-файла и объединение их в один DataFrame
    dfs = []
    for file in input_files:
        df = pd.read_csv(file)
        dfs.append(df)
    
    # объединение DataFrame'ов
    merged_df = pd.concat(dfs, ignore_index=True)
    
    # сохранение объединенных данных в CSV-файл
    merged_df.to_csv(output_file, index=False)
    print(f"Данные успешно объединены и сохранены в файл {output_file}")

# пример использования функции
merge_csv_files("merged_users.csv", "file1.csv", "file2.csv", "file3.csv")

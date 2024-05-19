from collections import Counter
import string


def process_text(text):
    # удаляем знаки пунктуации и приводим текст к нижнему регистру
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    # разделяем текст на слова
    words = text.split()
    return words

def main():
    file_path = 'example.txt'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = process_text(text)
            # считаем количество упоминаний каждого слова
            word_counts = Counter(words)
            # выводим наиболее часто встречающиеся слова
            print("Самые часто встречающиеся слова:")
            for word, count in word_counts.most_common(10):  # первые 10 самых часто встречающихся слов
                print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()

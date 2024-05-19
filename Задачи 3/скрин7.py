import string


def process_text(text):
    # Преобразуем текст в нижний регистр
    text = text.lower()
    # Удаляем знаки пунктуации
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Разбиваем текст на слова
    words = text.split()
    return words

def calculate_word_frequency(words):
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

def main():
    # Открываем файл для чтения
    with open('sample_text.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # Обрабатываем текст
    words = process_text(text)
    word_freq = calculate_word_frequency(words)

    # выводим статистику на экран
    print("Частота слов:")
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()

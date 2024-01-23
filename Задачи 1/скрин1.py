a=input('слова впиши')
words = [word.lower() for word in a.split()]
words.sort()
for word in words:
    print(word)
# объявление функции
def is_pangram(text):
    alphs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text = text.lower()
    for ch in text:
        if ch in alphs:
            alphs.remove(ch)
    return len(alphs) == 0


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))

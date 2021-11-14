def encrypt(text):
    words = []

    for word in text.split():
        new_word = ''
        word_len = len([c for c in word if c.isupper() or c.islower()])

        for char in word:
            if char.isupper():
                new_word += chr((ord(char) + word_len - 65) % 26 + 65)
            elif char.islower():
                new_word += chr((ord(char) + word_len - 97) % 26 + 97)
            else:
                new_word += char
        words.append(new_word)

    return ' '.join(words)


text = input()
word_len = -25
while word_len <= 0:
    word_len += 1
    print(encrypt(text))

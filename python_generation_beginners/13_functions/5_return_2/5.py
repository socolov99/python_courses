def is_one_away(word1, word2):
    count = 0
    flag = False

    if word1 == word2:
        return False

    if len(word1) != len(word2):
        return False

    for i in range(len(word1)):
        if word1[i] == word2[i]:
            count += 1
    if len(word1) - 1 == count:
        return True
    else:
        return False


txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))

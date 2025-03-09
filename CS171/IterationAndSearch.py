for letter in 'Gadsby':
    print(letter, end=' ')


def has_e(word):
    for letter in word:
        if letter == 'E' or letter == "e":
            return True
        return False


print()
print(has_e('Gadsby'))
print(has_e('Emma'))

print("#"*15)

file_object = open('words.txt')
print(file_object.readline())

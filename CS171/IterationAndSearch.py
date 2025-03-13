from doctest import run_docstring_examples
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
line = file_object.readline()
line2 = file_object.readline()
print(line)  # by book it should output "aa\n but python is now
# taking it as print statements \n when printing out."
print(line2)

word = line.strip()
print(word)

# strip removes whitespace characters –
# including spaces, tabs, and newlines
#  – from the beginning and end of the string.
print('####\n')

# for line in open('words.txt'):
#     word = line.strip()
#     print(word)

total = 0
count_e = 0
for line in open('words.txt'):
    word = line.strip()
    total += 1
    if has_e(word):
        count_e += 1

print(total)
print(count_e)


# The in Operator
word = "Gadsby"
print('e' in word)
print('b' in word)


def has_e(word):
    if 'E' in word or 'e' in word:
        return True
    return False

# OR


def has_e(word):
    return 'E' in word or 'e' in word

# OR


def has_e(word):
    return 'e' in word.lower()


print("####")
print(has_e('Gadsby'), has_e('Emma'))

print('\n', '#^'*14)


def uses_any(word, letters):
    """Checks if a word uses any of a list of letters.

    >>> uses_any('banana', 'aeiou')
    True
    >>> uses_any('apple', 'xyz')
    False
    """
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False


print(uses_any('banana', 'aeiou'), uses_any('apple', 'xyz'))
# TEST WITH DOCTEST


def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)


print(run_doctests(uses_any))  # If returns nothing FUNC IS WORKING CORRECT


def uses_any_incorrect(word, letters):
    """Checks if a word uses any of a list of letters.

    >>> uses_any_incorrect('banana', 'aeiou')
    True
    >>> uses_any_incorrect('apple', 'xyz')
    False
    """
    for letter in word.lower():
        if letter in letters.lower():
            return True
        else:
            return False     # INCORRECT EXAMPLE to show!


print(run_doctests(uses_any_incorrect))
# So as we can see it compares the provided answer with answer that it got.

# The structure of uses_any is similar to has_e. It loops through the letters in word and
# checks them one at a time. If it finds one that appears in letters, it returns True
# immediately. If it gets all the way through the loop without finding any, it returns False.
# This pattern is called a linear search. In the exercises at the end of this chapter, you’ll write
# more functions that use this pattern.

print("\/"*10, 'Exercizes')


def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.

    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('fanta', 'ad')
    False
    """
    for letter in word.lower():
        if letter in forbidden.lower():
            return False
    return True


print(run_doctests(uses_none))

print(uses_none('Huskar', 'zot'))
print(uses_none('Huskar', 'hot'))


def uses_only(word, available):
    """Checks whether a word uses only the available letters.

    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    """
    for letter in word.lower():
        if letter not in available.lower():
            return False  # If an invalid letter is found, return False
    return True  # If all letters are valid, return True


print(uses_only('banana', 'ban'))  # True
print(uses_only('apple', 'apl'))   # False


print()
print(uses_only('banana', 'ban'))
print(uses_only('apple', 'apl'))
print(uses_only('aaAAAA', 'apl'))
print(run_doctests(uses_only))

print()


def uses_all(word, required):
    """Checks whether a word uses all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    """
    for letter in required:
        if letter not in word:
            return False
    return True


print(run_doctests(uses_all))

print('>^<'*5, 'exercize')


def check_word(word, available, required):
    """Check whether a word is acceptable.

    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    if len(word) > 3:
        if required.lower() in word:
            for letter in word.lower():
                if letter not in available.lower():
                    return False
            return True
        elif required.lower() not in word:
            return False
    else:
        return False


print(run_doctests(check_word))

# OR in easier and Organized way:


def check_word(word, available, required):
    word = word.lower()
    available = available.lower()
    required = required.lower()
    if len(word) <= 3:
        return False

    if required not in word:
        return False

    for letter in word:
        if letter not in available:
            return False

    return True


print()


def word_score(word, available):
    """Compute the score for an acceptable word.

    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """
    pangram = True
    if len(word) == 4:
        return 1

    for letter in available.lower():
        if letter not in word.lower():
            pangram = False

    if len(word) > 4 and pangram == True:
        return len(word) + 7
    elif len(word) > 4:
        return (len(word))


print(run_doctests(word_score))

print('#'*10)


def uses_none(word, forbidden):
    """Checks whether a word avoids forbidden letters.

    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('', 'abc')
    True
    """
    return not uses_any(word, forbidden)


print(run_doctests(uses_none))

print('##########')


def uses_all(word, required):

    return uses_only(required, word)


print(uses_all('bananat', 'ban'))

print('##########')

# Here's what I got from ChatGPT 4o December 26, 2024
# It's correct, but it makes multiple calls to uses_any


def uses_all(s1, s2):
    """Checks if all characters in s2 are in s1, allowing repeats."""
    for char in s2:
        if not uses_any(s1, char):
            return False
    return True

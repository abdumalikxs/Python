import re
fruit = 'banana'
letter = fruit[1]

n = len(fruit)

print(fruit[n - 1])  # Notice the usage of -1 for indexing

print(fruit[0:3])  # 0 is included and 3 is excluded
print(fruit[:3])
print(fruit[3:6])
print(fruit[3:])

# If the first index is greater than or equal to the second, the result is an empty string, represented by two quotation marks:
print(fruit[3:3])

print()


greeting = 'Hello, world!'
# greeting[0] = 'J' cant do it cuz its immutable


new_greeting = 'J' + greeting[1:]
print(new_greeting)

print(greeting)
print()

word = 'banana'

if word == 'banana':
    print('All right, banana.')

print()


def compare_word(word):
    if word < 'banana':
        print(word, 'comes before banana.')
    elif word > 'banana':
        print(word, 'comes after banana.')
    else:
        print('All right, banana.')


compare_word('apple')
compare_word('bcnana')  # Good for Journal letter going

# strinbg methods

word = 'banana'
new_word = word.lower(), word.upper()
print(new_word)


# Writing Files
a = 'Helllo world'
print(a.startswith('Helllo'))
print()
reader = open('pg345.txt')


def is_special_line(line):
    return line.startswith('*** ')


for line in reader:
    if is_special_line(line):
        print(line.strip())

print()
# we need to open it againb cuz thge pointer went already to the end of file.
reader = open('pg345.txt')
writer = open('pg345_cleaned.txt', 'w')

for line in reader:
    if is_special_line(line):
        # When the loop exits, line contains the special line that made the conditional true.
        break
    # we can use it later
print(line)

# Because reader keeps track of where it is in the file, we can use a second loop to pick up where we left off.
for line in reader:
    if is_special_line(line):
        break
    writer.write(line)

print(line)  # When this loop exits, line contains the second special line.

# To indicate that we’re done, we can close both files by invoking the close method.
reader.close()
writer.close()

# checking :
for line in open('pg345_cleaned.txt'):
    line = line.strip()
    if len(line) > 0:
        print(line)
    if line.endswith('Stoker'):
        break
print('@')
print(line)

count = 0
for line in open('pg345_cleaned.txt'):
    count += 1
print('lines:', count)

counter = 0
for line in open('pg345_cleaned.txt'):
    chars = len(line.strip())
    counter += chars
print('chars:', counter)
# Find and replace

# OR
counter = 0
for line in open('pg345_cleaned.txt'):
    lines = line.strip()
    for chars in lines:
        counter += 1
print('chars:', counter)

print("#"*14)

total = 0
for line in open('pg345_cleaned.txt'):
    total += line.count('Jonathan')

print(total)

# Replacing:
writer = open('pg345_replaced.txt', 'w')

for line in open('pg345_cleaned.txt'):
    line = line.replace('Jonathan', 'Thomas')
    writer.write(line)
# Done


print('\n Regular Expressions')

# A module called re provides functions related to regular expressions.

text = "I am Dracula; and I bid you welcome, Mr. Harker, to my house."

pattern = 'Dracula'

result = re.search(pattern, text)
print(result)
# If the pattern appears in the text, search returns a Match object that contains the results of the search.
# Among other information, it has a variable named string that contains the text that was searched.
print(result.string)
# It also provides a method called group that returns the part of the text that matched the pattern.
print(result.group())
# And it provides a method called span that returns the index in the text where the pattern starts and ends.
print(result.span())


# If the pattern doesn’t appear in the text, the return value from search is None.
result = re.search('Count', text)
print(result)
# So we can check whether the search was successful by checking whether the result is None.
print(result == None)

####
print()


def find_first(pattern):
    for line in open('pg345_cleaned.txt'):
        result = re.search(pattern, line)
        if result != None:
            return result


result = find_first('Harker')
print(result.string)

# For example, if the pattern includes the vertical bar character, '|',
# it can match either the sequence on the left or the sequence on the right.
# Suppose we want to find the first mention of Mina Murray in the book,
#  but we are not sure whether she is referred to by first name or last.
# We can use the following pattern, which matches either name.

# re.search is good cuz :
# The | (pipe) in regex (re.search()) acts as an "OR" operator,
#  allowing you to search for multiple patterns at once.

pattern = 'Mina|Murray'
result = find_first(pattern)
print(result.string)


# We can use a pattern like this to see how many times a character is mentioned by either name.
# Here’s a function that loops through the book and counts the number of lines that match the given pattern.

def count_matches(pattern):
    count = 0
    for line in open('pg345_cleaned.txt'):
        result = re.search(pattern, line)
        if result != None:
            count += 1
    return count


print(count_matches('Mina|Murray'))

# The special character '^' matches the beginning of a string, so we can find a line that starts with a given pattern.

result = find_first('^Dracula')
print(result.string)

# And the special character '$' matches the end of a string,
# so we can find a line that ends with a given pattern (ignoring the newline at the end).

result = find_first('Harker$')
print(result.string)

# String is considereed an attribute of re module in this case


print('STRING SUBSTITUTION')

pattern = 'cent(er|re)'

result = find_first(pattern)
print(result.string)

# We can also check whether he used the British spelling of “colour”.
#  The following pattern uses the special character '?', which means that the previous character is optional.
pattern = 'colou?r'
result = find_first(pattern)
line = result.string
print(line)


# Now suppose we want to produce an edition of the book with American spellings.
# We can use the sub function in the re module, which does string substitution.

print(re.sub(pattern, 'color', line))

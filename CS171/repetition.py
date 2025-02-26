import think
for i in range(10):
    print(i)
print()
for i in range(10):
    print(i+1)
#####
print('stop')


def repeat(word, n):
    for i in range(n):
        print(word, end=", ")


repeat('challenge', 5)

print('\n\nstop\n')


def printer(text, dist):
    for i in range(dist):
        print(" ", end="")
    print(text)


printer('lol', 10)
printer('ok', 10)

print('\nstop\n')


def prt(text, dist):
    space = dist * ' '
    print(space + text)


prt('lol', 10)
prt('ok', 10)

print('\nstop\n')


def pyramid(char, n):
    for i in range(n):
        print((i + 1) * char)


pyramid('L', 5)

print('\nstop\n')


def rect(char, a, b):
    for i in range(b):
        print(char * a)


rect("H", 5, 4)

print('\nstop\n')


def bottle_verse(n):
    print(f'{n} bottles of beer on the wall')
    print(f"{n} bottles of beer ")
    print('Take one down, pass it around')
    print(f'{n-1} bottles of beer on the wall')


for n in range(99, 0, -1):
    bottle_verse(n)
    print()

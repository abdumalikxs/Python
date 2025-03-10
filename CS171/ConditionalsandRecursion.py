from time import time, sleep
a = -11 and True
print(a)

b = 21 and True
print(b)
# Strictly speaking, the operands of a logical operator
# should be boolean expressions, but Python is not
# very strict. Any nonzero number is interpreted as True:

####
x = 1
y = 2

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

# OR WE COULD USE: NESTED CONDITIONALS
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
# Recursion


def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)


countdown(5)
#####


def printer(text, n):
    if n > 0:
        print(text, end=" ")
        printer(text, n-1)


printer('jengo', 4)
print('\n')
for i in range(4):
    print('jengo', end=' ')
####


def countdown_by_two(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown_by_two(n-2)


countdown_by_two(6)
countdown_by_two(5)
print('')
########


def starter():
    while True:
        now = time()
        years = now // (60 * 60 * 24 * 365)
        r = now % (60 * 60 * 24 * 365)
        days = r // (60 * 60 * 24)
        rr = r % (60 * 60 * 24)
        hours = rr // (60 * 60) - 5
        rrr = rr % (60 * 60)
        minutes = rrr // 60
        seconds = rrr - (minutes * 60)

        print(f"{int(years)} years, {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds.", end="\r")
        sleep(1)

######


def is_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        print('No')
    else:
        print("Yes")


is_triangle(5, 5, 100)

######

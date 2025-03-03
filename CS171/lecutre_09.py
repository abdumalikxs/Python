def whatever():
    print("Hi")


def bats(x):
    if x > 5:
        return [9, True]
    return [10, False]


def cats(x):
    if x % 2 == 0:
        return  # return without value returns 'None' or could do return None directly
    return 9


x = whatever()
if x == None:
    print("That function did nothing.")
List = bats(12)  # 'A' and 'B' be take the values from the list.
print(List[0])
print(List[1])


print()
z, t, y = [3, 4, True]
print(z)
print(t)
print(y)
print()
for i in range(0, 10):
    print(i, cats(i))

print('*'*50)


def coolFunc(a=15, b=9, c=12):
    return a*b - c


print(coolFunc(1, 2, 3))
# If given value it will use that one , if not it will use the assigned value in parameters
print(coolFunc(5, 6))
print(coolFunc(1))
print(coolFunc())
# Can use this when messy, it will give these values and will use these values even if indicated otherwise in the parameters
print(coolFunc(c=1, b=3))

###########


def f(a, b):
    global c
    print("in f a =", a)
    print("in f b =", b)
    a = a + 1
    c = c + 1
    return h(b, a)


def h(b, c):
    '''
    This function was defined to trick students.

    '''
    print('In h a =', a)
    print("In h b =", b)
    print("In c =", c)
    return a+b+c


help(h)
help(f)
help(print)
a = 10
b = 12
c = 13

f(7, 9)
print("In Main a =", a)
print("In Main b =", b)
print("In Main c =", c)

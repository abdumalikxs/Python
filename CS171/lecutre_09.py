def whatever():
    print("Hi")


def bats(x):
    if x > 5:
        return [9, True]
    return [10, False]


def cats(x):
    if x % 2 == 0:
        return
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

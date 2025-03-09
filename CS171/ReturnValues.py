import math


def repeat(word, n):
    print(word * n)


result = repeat("finland, ", 3)
print()
print(result)


def repeat_string(word, n):
    return word * n


print()

line = repeat_string('Spam, ', 4)
print(line)
#############
print()

print("#"*15, 'factorial function')


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))

print('#'*15 + ' Fibonacci')


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


print(fibonacci(6))

print("######## Isinstance")
a = 13.5

print(isinstance(a, (float and int)))
print(isinstance(a, (float or int)))
print(isinstance(a, float))


def factorial(n):
    if not isinstance(n, int):
        print('factorial is only defined for integers.')
        return None
    elif n < 0:
        print('factorial is not defined for negative numbers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(-3))
print(factorial(-3.5))
print(factorial('crunchy frog'))


def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(space, 'returning', result)
        return result


factorial(5)

print('\n#'*3, 'Exercises')


def hypot(a, b):
    return math.sqrt(a**2+b**2)


print(hypot(3, 4))

print('\n', "#"*3, 'brr')


def is_between(x, y, z):
    if x <= y <= z or z >= y >= x:
        return True
    return False


def is_between(x, y, z):
    return x <= y <= z or z >= y >= x


print('\n', "#"*3, 'brr')


def A(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return A(m-1, 1)
    elif m > 0 and n > 0:
        return A(m-1, A(m, n-1))


# print(A(5, 5)) Will Result in recursion error
print(A(3, 3))


print('\n', "#"*3, 'brr')


def gcd(a, b):
    if b == 0:
        return a  # Base case: when remainder is 0, a is the GCD
    return gcd(b, a % b)  # Recursive call following the Euclidean algorithm


print(gcd(8, 12))  # ✅ Output: 4
print(gcd(18, 27))  # ✅ Output: 9
print(gcd(101, 103))  # ✅ Output: 1 (since they are prime)

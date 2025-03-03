import random


def runSomeTests(size):
    X = []
    for i in range(0, size):
        X.append(random.randint(0, 2*size))
    X.sort()
    totalTests = 0
    totalCount = 0
    for i in range(0, 2*size):
        a, b = linearSearch(X, i)
        totalTests += 1
        totalCount += b
    return totalCount/totalTests


def binarySearch(haystack, needle, start=None, stop=None):
    print("I am looking for", needle)
    print("I am searching", haystack)
    print(start, stop)
    if start == None:
        start = 0
    if stop == None:
        stop = len(haystack)-1
    if start > stop:
        return [False, 0]
    middle = start + (stop-start)//2
    print("Middle", middle)
    if needle == haystack[middle]:
        return [True, 1]
    if needle < haystack[middle]:
        a, b = binarySearch(haystack, needle, start, middle-1)
        return [a, b+1]
    else:
        a, b = binarySearch(haystack, needle, middle+1, stop)
        return [a, b+1]


def linearSearch(haystack, needle):
    count = 0
    for i in range(0, len(haystack)):
        count += 1
        if needle == haystack[i]:
            return [True, count]
        if needle < haystack[i]:
            return [False, count]
    return [False, count]


if __name__ == '__main__':
    for i in range(0, 11):
        size = 2**i
        a = runSomeTests(size)
        print(f"Size: {size} Linear: {a}")

    print(binarySearch([1, 2, 3, 4, 5, 6, 7], 100))

# its Awab's code

import time


def readWords(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
    return lines  # Called insertion sort


def swap(data, i, j):
    print(f'swapping {i} and {j}')
    temp = data[i]
    data[i] = data[j]
    data[j] = temp
    return


def insertInto(data, pos):
    while pos > 0 and data[pos] < data[pos - 1]:
        swap(data, pos, pos - 1)
        pos -= 1
    return


def insertionSort(data):
    for i in range(1, len(data)):
        insertInto(data, i)
    print(data)
    return


if __name__ == "__main__":
    filename = 'words.txt'
    # target = readWords(filename)
    # print(target)
    before = time.time()
    example = [5, 3, 4, 2, 1]
    insertInto(example, 1)
    print(example)
    insertInto(example, 2)
    print(example)
    insertInto(example, 3)
    print(example)
    insertInto(example, 4)
    print(example)
    after = time.time()
    print(after - before)

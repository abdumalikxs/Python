from lecture10 import swap


def partition(data, start, stop):
    pivot = data[stop]
    firstLarger = start
    i = start
    while i <= stop:
        if data[i] > pivot:
            i = i + 1   # Move Forward
        else:
            swap(data, i, firstLarger)
            i = i + 1  # Mover Forward
            firstLarger += 1  # We used that larger value
    return firstLarger - 1


def quicksort(data, start, stop):
    print("Sorting", data, start, stop)
    if start >= stop:
        return
    p = partition(data, start, stop)
    print("The pivot ended up at", p)
    quicksort(data, start, p-1)
    quicksort(data, p+1, stop)


if __name__ == "__main__":
    L = [7, 1, 8, 2, 6, 4, 5]
    quicksort(L, 0, 6)
    print(L)

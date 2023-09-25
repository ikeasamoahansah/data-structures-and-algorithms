def insertion_sort(a: list):
    n = len(a)
    i = 1
    while i < n:
        current = a[i]
        j = i - 1
        while j >= 0 and a[j] > current:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = current
        i = i + 1
    return a

print(insertion_sort(a=[68, 72, 12, 34, 65, 90, 2, 38]))

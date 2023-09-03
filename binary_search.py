import math
# Implementing linear search

# def linear_search(a:list, target:int):
#     """ A single WHILE loop iterates over each element of the array, and the internal
#         IF statement compares that element to the target. As soon as we come
#         across an element matching the target, we return the corresponding index. If
#         we make it to the end of the array, we return -1."""
#     i = 0
#     while i < len(a):
#         if a[i] == target:
#             return True
#         i = i + 1
#     return False

# a = [3, 21, 5, 6, 7, 8]
# target = 0
# print(linear_search(a, target))


# Implementing Binary Search Algorithm

def binary_search(a:list, target:int):
    index_low = 0
    index_high = len(a) - 1

    while index_low <= index_high:
        index_mid = math.floor((index_low+index_high)/2)
        if a[index_mid] == target:
            return index_mid
        if a[index_mid] < target:
            index_low = index_mid + 1
        else:
            index_high = index_mid - 1
    return False
        
a = [2, 3, 5, 7, 11, 13, 17, 19]
target = 20
print(binary_search(a, target))
    
# log base 2 to the N
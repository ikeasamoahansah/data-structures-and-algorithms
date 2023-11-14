import array as arr

class Stack:
    
    def __init__(self, array_size, array, top=-1) -> None:
        self.array_size = array_size
        self.top = top
        self.array = array


def push(s : Stack, value):
    if s.top == s.array_size - 1:
        print("Exceeded")
    s.top = s.top + 1
    s.array[s.top] = value
    return s.array

a = arr.array('i', [1, 4, 5])

s = Stack(array_size=7, array=a)
print(push(s=s, value=7))

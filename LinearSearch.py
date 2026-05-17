array = [1, 2, 4, 5, 6, 7, 5, 1, 2]
target = 5

def linear(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

print(linear(array, target))
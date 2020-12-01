from builtins import print

def majority_element(arr1):
    count = 0
    candidate = None
    for n in arr1:
        if count == 0:
            candidate = n
        count += 1
        if n != candidate:
            count -= 1
    return candidate


arr = [4, 8, 1, 1, 6, 1, 2]
result = majority_element(arr)
print(result)

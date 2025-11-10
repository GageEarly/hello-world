def isSorted(lst):
    if len(lst) < 2:
        return True
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

if __name__ == "__main__":
    print(isSorted([]))
    print(isSorted([1]))
    print(isSorted([1, 2, 2, 3]))
    print(isSorted([5, 3, 2]))
    print(isSorted([5, 4, 3, 2, 1]))
    print(isSorted([2, 2, 2, 2]))

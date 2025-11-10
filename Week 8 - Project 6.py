def myRange(start, stop=None, step=None):
    if stop is None:
        start, stop = 0, start
    if step is None:
        step = 1
    if step == 0:
        print ("step cannot be zero.")
    nums = []
    i = start
    if step > 0:
        while i < stop:
            nums.append(i)
            i += step
    else:
        while i > stop:
            nums.append(i)
            i += step
    return nums

print(myRange(5))
print(myRange(2, 6))
print(myRange(10, 2, -2))
print(myRange(1, 10, 3))

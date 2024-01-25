def f(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start == 10:
        return 0
    if start < end:
        return f(start + 1, end) + f(start + 5, end) + f(start * 2, end)
print(f(1,8)*f(8,16))

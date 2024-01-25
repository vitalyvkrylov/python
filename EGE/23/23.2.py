def f(start, end, pr):
    if start == end:
        return 1
    if start > end:
        return 0
    if start < end:
        if pr == 0:
            return f(start + 1, end, 0) + f(start + 2, end, 0) + f(start * 2, end, 1)
        if pr == 1:
            return f(start + 1, end, 0) + f(start + 2, end, 0)
print(f(1,9,0))

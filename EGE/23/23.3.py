def f(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    if start == 24:
        return 0
    if start < end:
        return f(start + 1,end) + f(2 * start + 1, end)
    if start == 24:
        return 0
print(f(1,25))

def find_max_min(arr):
    x = min(arr)
    y = max(arr)
    if x == y:
        return [len(arr)]
    else:
        return [x, y]


# print find_max_min([6, 6, 6])

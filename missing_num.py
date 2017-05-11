def find_missing(A, B):
    result = 0
    C = A + B
    for num in C:
        if C.count(num) % 2 != 0:
            result = num
    return result
    # for num in C:
    #     if num in A and num in B:
    #         pass
    #     else:
    #         return num
    # return result


print (find_missing([9, 9, 7, 6, 5, 3, 4, 2, 1], [9, 7, 6, 5, 3, 4, 2, 1, 8]))
print (find_missing([2], [2]))

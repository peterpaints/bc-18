# -*- coding: utf-8 -*-


def words(string):
    string = string.split()
    for i in range(len(string)):
        try:
            if isinstance(int(string[i]), int):
                string[i] = int(string[i])
        except Exception:
            continue
    count = {}
    for word in string:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    return count


print (words('¡Hola! ¿Qué tal? Привет!'))

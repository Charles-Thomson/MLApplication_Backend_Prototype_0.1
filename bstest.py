listl = [1, 2, 3]


def test():
    try:
        value = listl[2]
    except IndexError:
        value = 0
    return value


thisvalue = test()
print(thisvalue)

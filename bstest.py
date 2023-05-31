listl = [1, 2, 3]


def test():
    try:
        value = listl[-2]
        return value
    except IndexError:
        return 0


thisvalue = test()
print(thisvalue)

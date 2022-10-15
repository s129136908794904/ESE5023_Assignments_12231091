# Algorithm and code independently designed by Shao Shi

def Print_values(a, b, c):
    if a > b:
        if b > c:
            return compute(a, b, c)
        else:
            if a > c:
                return compute(a, c, b)
            else:
                return compute(c, a, b)
    else:  # a<=b
        if not b > c:
            return compute(c, b, a)


def compute(x, y, z):
    return x + y - 10 * z

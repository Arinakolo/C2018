python
def factorial(numn):
    if numn < 0:
        return None
    elif numn == 0:
        return 1
    else:
        result = 1
        for i in range(1, numn + 1):
            result *= i
        return result
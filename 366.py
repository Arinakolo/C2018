result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a must be bigger than or equal to b")
        if b == 0:
            raise ZeroDivisionError("b must not be equal zero")
        if b > 100:
            raise IndexError("b must not be bigger than 100")
        return a/b
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")
    except IndexError as ie:
        print(f"IndexError: {ie}")

znay = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key in znay:
    res = divider(key, znay[key])
    result.append(res)
print(result)
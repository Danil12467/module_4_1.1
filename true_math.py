from math import inf
def divide(first, second):
    num1 = first
    num2 = second
    if second == 0:
        return inf
    else: res = num1 / num2
    return res
print(divide(22,4))
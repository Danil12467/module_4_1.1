def divide(first, second):
    error = "Ошибка"
    num1 = first
    num2 = second
    if second == 0:
        return error
    else: res = num1 / num2
    return res
print(divide(4,0))
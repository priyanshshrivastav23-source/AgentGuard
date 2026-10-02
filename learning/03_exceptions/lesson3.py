def divide_numbers(a:float,b:float)->float:

    try:
        result = a/b
    except ZeroDivisionError:
        return {"Division by zero is not allowed"}
    else:
        return result

print(divide_numbers(10,2))
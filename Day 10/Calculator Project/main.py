def add(n1, n2):
    """ addition of two numbers"""
    return n1 + n2


def subtract(n1, n2):
    """ subtraction of two numbers"""
    return n1 + n2

def divide(n1, n2):
    """ division of two numbers"""
    return n1 + n2

def multi(n1, n2):
    """ multiplication of two numbers"""
    return n1 + n2


operation = {
    "-": subtract,
    "/": divide,
    "*": multi,
    "+": add
}

print(operation["-"](20, 15))
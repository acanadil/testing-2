class Calculator:

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        #comment
        return x * y

    def divide(x, y):
        if y == 0:
            return 'Can\'t divide by 0'
        return x * 1.0 / y

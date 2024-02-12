class Calculator:

    def add(x, y):
        return bin(x + y)

    def subtract(x, y):
        return bin(x - y)

    def multiply(x, y):
        #
        return bin(x * y)

    def divide(x, y):
        if y == 0:
            return 'Can\'t divide by 0'
        return bin(x * 1.0 / y)

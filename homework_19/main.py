# main.py
class Functions:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def is_even(self, n):
        return n % 2 == 0

    def is_odd(self, n):
        return n % 2 != 0

    def is_positive(self, n):
        return n > 0

    def is_negative(self, n):
        return n < 0

    def is_zero(self, n):
        return n == 0

    def is_positive_or_zero(self, n):
        return n >= 0

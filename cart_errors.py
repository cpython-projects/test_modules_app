class PriceError(Exception):

    def __init__(self, price_value):
        self.price_value = price_value

    def __str__(self):
        return f'Expected positive number, but got {self.price_value}'


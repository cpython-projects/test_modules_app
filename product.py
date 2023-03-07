from cart_errors import PriceError

class Product:

    def __init__(self, title: str, price: float | int):
        if not isinstance(price, float | int):
            raise TypeError()
        if price <= 0:
            raise PriceError(price)

        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price:.2f}'


if __name__ == '__main__':
    pr_1 = Product('banana', 40)
    pr_2 = Product('apple', 45)
    pr_3 = Product('orange', -50)

    print(pr_1, pr_2, pr_3, sep='\n')
from product import Product


class Cart:

    def __init__(self):
        self.__products = []
        self.__quantities = []

    def add_product(self, product: Product, quantities=1):
        if not isinstance(product, Product):
            raise TypeError()
        if not isinstance(quantities, int | float):
            raise TypeError()
        if quantities <= 0:
            raise ValueError()

        self.__products.append(product)
        self.__quantities.append(quantities)

    def total(self):
        return sum(product.price * quantity for product, quantity in zip(self.__products, self.__quantities))

    def __str__(self):
        res = [f'{product} x {quantity} = {product.price * quantity}' for product, quantity in zip(self.__products, self.__quantities)]
        return '\n'.join(res)


if __name__ == '__main__':
    pr_1 = Product('banana', 40)
    pr_2 = Product('apple', 45)
    pr_3 = Product('orange', 50)

    order = Cart()
    order.add_product(pr_1, 2)
    order.add_product(pr_2, 3)
    order.add_product(pr_3, 1)

    print(order)
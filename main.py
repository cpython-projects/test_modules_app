import product
import cart
import cart_errors


def main():
    try:
        pr_1 = product.Product('banana', 40)
        pr_2 = product.Product('apple', 45)
        pr_3 = product.Product('orange', 50)

        order = cart.Cart()
        order.add_product(pr_1, 2)
        order.add_product(pr_2, -3)
        order.add_product(pr_3, 1)

        print(order)
    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()
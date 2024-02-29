class CashRegister:

    def __init__(self, cashier):
        self.cashier = cashier
        self._products = dict()

    def add_product(self, product, quantity=1):
        if product['name'] in self._products:
            self._products[product['name']]['quantity'] += quantity
        else:
            self._products[product['name']] = {
                'price': product['price'],
                'quantity': quantity
            }

    def remove_product(self, product, quantity=1):
        if product['name'] not in self._products:
            raise ProductNotFoundError
        if quantity >= self._products[product['name']]['quantity']:
            del self._products[product['name']]
        else:
            self._products[product['name']]['quantity'] -= quantity

    def list_products(self):
        return self._products

    def update_price(self, product, price):
        if product['name'] not in self._products:
            raise ProductNotFoundError
        self._products[product['name']]['price'] = price

    def calculate_tax(self):
        return round(self.total() * 0.05, 2)

    def total(self, with_tax=False):
        total = sum(
            p['price'] * p['quantity'] for p in self._products.values()
        )
        if with_tax:
            total += self.calculate_tax()
        return total

    def clear(self):
        self._products = dict()


class ProductNotFoundError(Exception):
    pass

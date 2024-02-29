import unittest
from register import CashRegister, ProductNotFoundError


class TestCashRegister(unittest.TestCase):

    def setUp(self):
        self.register = CashRegister('Samantha')
        self.eggs = {'name': 'eggs', 'price': 2.99}

    def add_eggs(self, quantity=1):
        self.register.add_product(self.eggs, quantity=quantity)

    def test_has_attribute_cashier_name(self):
        self.assertEqual('Samantha', self.register.cashier)

    def test_can_add_and_list_products(self):
        self.add_eggs()
        self.assertEqual(
            {'eggs': {'price': self.eggs['price'], 'quantity': 1}},
            self.register.list_products()
        )

    def test_can_add_multiple_products(self):
        self.add_eggs(2)
        self.assertEqual(2, self.register.list_products()['eggs']['quantity'])

    def test_can_remove_products(self):
        self.add_eggs()
        self.register.remove_product(self.eggs)
        self.assertEqual(dict(), self.register.list_products())

    def test_can_remove_multiple_products(self):
        self.add_eggs(2)
        self.register.remove_product(self.eggs, 2)
        self.assertEqual(dict(), self.register.list_products())

    def test_cannot_remove_product_if_not_added(self):
        with self.assertRaises(ProductNotFoundError):
            self.register.remove_product(self.eggs)

    def test_can_update_price_of_added_product(self):
        self.add_eggs()
        self.register.update_price(self.eggs, 0.50)
        self.assertEqual(
            0.50,
            self.register.list_products()['eggs']['price']
        )

    def test_cannot_update_price_of_if_product_not_added(self):
        with self.assertRaises(ProductNotFoundError):
            self.register.update_price(self.eggs, 0.50)

    def test_calculate_total_without_tax(self):
        self.add_eggs()
        self.assertEqual(2.99, self.register.total())

    def test_calculate_tax(self):
        self.add_eggs()
        self.assertEqual(0.15, self.register.calculate_tax())

    def test_calculate_total_with_tax(self):
        self.add_eggs()
        self.assertEqual(3.14, self.register.total(with_tax=True))

    def test_clear_products(self):
        self.add_eggs()
        self.register.clear()
        self.assertEqual(dict(), self.register.list_products())


if __name__ == '__main__':
    unittest.main()

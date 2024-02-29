# TODO

- [x] product = dict.fromkeys(['name', 'price'])  # create 3 products
- [x] CashRegister.cashier_name
- [x] CashRegister.add_product(product, count=1)
- [x] .list_products()
- [x] .add_product(product, 2)  # how to deal with duplicate products
- [x] .remove_product(product, count=1)
- [x] .remove_product(product, 2)  # remove multiple products
- [x] .update_price(product, price) # 'product' must be already added
- [x] .update_price raises exception if product not added
- [x] .total(with_tax=False)
- [x] .calculate_tax(percentage=5)
- [x] .total(with_tax=True)
- [x] .clear()
- [x] Implement CashRegister._products as a dict
- [x] Can't remove product not in register
- [ ] Store products in an sqlite3 database
- [ ] Add a cli
- [ ] Add a web front end

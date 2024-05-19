class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def increase_quantity(self, amount):
        self.quantity += amount

    def decrease_quantity(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            print("Ошибка: недостаточное количество товара")

    def calculate_total_price(self):
        return self.price * self.quantity


# пример использования класса
product1 = Product("Молоко", 2.5, 10)
product2 = Product("Хлеб", 1.0, 5)

# увеличение количества товара
product1.increase_quantity(5)
product2.increase_quantity(3)

# уменьшение количества товара
product1.decrease_quantity(2)
product2.decrease_quantity(6)

# расчет общей стоимости товара
total_price_product1 = product1.calculate_total_price()
total_price_product2 = product2.calculate_total_price()

print(f"Общая стоимость товара '{product1.name}': ${total_price_product1}")
print(f"Общая стоимость товара '{product2.name}': ${total_price_product2}")


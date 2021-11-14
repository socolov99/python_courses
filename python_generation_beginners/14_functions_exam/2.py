# объявление функции
def get_shipping_cost(quantity):
    price = 0
    if quantity > 0:
        price += 1000
    if quantity > 1:
        price += 120 * (quantity - 1)
    return price


# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))

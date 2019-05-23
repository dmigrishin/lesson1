def format_price(price):
    price = int(price)
    price = 'Цена: {} рублей'.format(price)
    return price

price = 56.24
result = format_price(price)
print (result)
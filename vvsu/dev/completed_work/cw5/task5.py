# Задание 5
groceries = {
    'банан': 50,
    'курица': 23,
    'ананас': 450,
    'бульба': 12,
    'гашиш': 250
}

max_name, max_price = max(groceries.items(), key=lambda item: item[1])
min_name, min_price = min(groceries.items(), key=lambda item: item[1])

print(f'Максимальная цена у - {max_name}, и равна: {max_price}')
print(f'Минимальная цена у - {min_name}, и равна: {min_price}')

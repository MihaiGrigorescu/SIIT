articles = ["shirt", "scarf", "glove", "heat", "pants", "blouse"]
sizes = ["S", "M", "L", "XL", "XXL"]
number_items = 500

shop = [(articles[i % len(articles)], sizes[i % len(sizes)]) for i in range(number_items)]

print(shop)
# sell the latest article using pop
print(shop.pop())
# sell any item by removing it, either by index or by the item itself
shop.remove(shop[1])
shop.remove(("shirt", "XXL"))
print(shop)
# restock the shop using append
shop.append((articles[4], sizes[1]))
print(shop)

def add_item(item, items=[]):
    items.append(item)
    return items

cart = add_item("apple")
add_item("banana")
print(cart)
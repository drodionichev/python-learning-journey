# Кортеж — это как список, но неизменяемый:
point = (10, 20)
print(point[0])   # 10 — индексы работают как у списка

# point[0] = 99   # TypeError — менять нельзя

# зачем нужно то что нельзя менять?
# Три причины:
#
# 1. Защита от случайных изменений — координаты, настройки, то что не должно меняться
# 2. Кортеж можно использовать как ключ словаря, а список нельзя
# 3. Распаковка: name, domain = email.split("@") — справа технически кортеж

locations = {
    (55.7, 37.6): "Moscow",
    (40.7, -74.0): "New York"
}
print(locations[(55.7, 37.6)])

# Ещё одна фишка кортежей — возврат нескольких значений из функции:
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([5, 2, 8, 1])
print(low, high)   # 1 8

# Функция как будто возвращает
# два значения, а на деле один кортеж, который ты сразу распаковываешь.

# Set — это коллекция уникальных элементов, без порядка:
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)   # {1, 2, 3} — дубликаты исчезли

# Главная фишка — автоматически убирает повторы. Отсюда самое частое применение:
emails = ["a@x.com", "b@x.com", "a@x.com"]
unique = set(emails)
print(unique)        # {'a@x.com', 'b@x.com'}
print(len(unique))   # 2

# В выводе set порядок другой (b раньше a).
# Это потому что set неупорядочен, элементы лежат как попало.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)   # пересечение — что в обоих: {3, 4}
print(a | b)   # объединение — всё вместе: {1,2,3,4,5,6}
print(a - b)   # разница — что в a но не в b: {1, 2}

# Теперь задачка чтобы закрепить.
# Напиши функцию find_duplicates(items) которая принимает список
# и возвращает set элементов которые встречаются больше одного раза.

def find_duplicates(items):
    result = {}
    for item in items:
        result[item] = result.get(item, 0) + 1
    duplicates = set()
    for key, value in result.items():
        if value > 1:
            duplicates.add(key)
    return duplicates
print(find_duplicates([1, 2, 2, 3, 3, 3, 4]))

def compare_api_response(expected, actual):
    result = {
        "missing": (set(expected) - set(actual)),
        "extra": (set(actual) - set(expected)),
    }
    return result
print(compare_api_response(["id", "name", "email"], ["id", "name", "phone"]))
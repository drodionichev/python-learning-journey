#Задача 1: Анализатор слов
#Напиши функцию analyze_words(words), возвращает словарь:
import collections


#{
#    "total": количество слов,
#    "longest": самое длинное,
#    "shortest": самое короткое,
#    "average_length": средняя длина (round до 1 знака),
#    "uppercase": список в верхнем регистре
#}

# def analyze_words(words):
#     return {
#         "total": len(words),
#         "longest": max(words, key=len),
#         "shortest": min(words, key=len),
#         "average_length": round(sum(len(word) for word in words) / (len(words)),1),
#         "uppercase": [word.upper() for word in words],
#     }
#
# print(analyze_words(["apple", "banana", "kiwi"]))
# # {'total': 3, 'longest': 'banana', 'shortest': 'kiwi', 'average_length': 5.0, 'uppercase': ['APPLE', 'BANANA', 'KIWI']}
#
# print(analyze_words(["hello", "hi", "python", "code"]))
# {'total': 4, 'longest': 'python', 'shortest': 'hi', 'average_length': 4.2, 'uppercase': ['HELLO', 'HI', 'PYTHON', 'CODE']}

#Задача 2: Подсчёт частоты букв
# Напиши функцию count_letters(text), которая принимает строку и возвращает
# словарь где ключ — буква, значение — сколько раз встречается.

# Идея: проходишь по элементам, для каждого либо добавляешь
# в словарь со значением 1, либо увеличиваешь существующее значение.

def count_letters(text):
    result = {} # Сначала создаем пустой словарь
    for i in text: # Идем по каждой букве
        result[i] = text.count(i) # Считаем эту букву и кладем в словарь
    return result

# # Проверяем:
print(count_letters("hello"))
# Выдаст: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def count_letters(text):
    result = {}
    clean_text = text.lower()
    for char in clean_next:
        result[char] = result.get(char, 0) + 1
    return result

def count_food(items):
    result = {}
    for item in items:
        name = item.lower()
        result[name] = result.get(name, 0) + 1
    return result
my_shopping_list = ['Apple', 'banana', 'apple', 'Orange', 'banana', 'apple']
print(count_food(my_shopping_list))

def count_long_names(names):
    result = {}
    for item in names:
        clean_name = item.lower()
        if len(clean_name) > 3:
            result[clean_name] = result.get(clean_name, 0) + 1
    return result
test_names = ['Alex', 'Bo', 'Alex', 'Anna', 'Jo', 'Anna']
print(count_long_names(test_names))


print(count_letters("hello"))
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

print(count_letters("banana"))
# {'b': 1, 'a': 3, 'n': 2}

print(count_letters(""))
# {}
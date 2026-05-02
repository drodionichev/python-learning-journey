# fruits = ["apple", "banana", "cherry"]
# fruits[0]              # "apple"
# fruits[-1]             # "cherry"
# fruits.append("orange") # добавить в конец
# len(fruits)            # длина
#
# # Section 1: list basics
# fruits = ["apple", "banana", "cherry"]
# print(fruits)
# print(fruits[0])
# print(fruits[-1])
# print(len(fruits))

# # Section 2: modifying lists
# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")        # добавить в конец
# print(fruits)
#
# fruits.insert(0, "kiwi")       # вставить на позицию 0 (в начало)
# print(fruits)
#
# fruits.remove("banana")        # удалить по значению
# print(fruits)
#
# last = fruits.pop()            # удалить и вернуть последний
# print(last)
# print(fruits)
#
# fruits[0] = "lemon"            # заменить по индексу
# print(fruits)

# # Section 3: sorting
# numbers = [5, 2, 8, 1, 9, 3]
# numbers.sort()
# print(numbers)
#
# numbers.sort(reverse=True)
# print(numbers)
#
# words = ["banana", "apple", "cherry"]
# words.sort()
# print(words)
#
# numbers.sort()              # меняет сам список, ничего не возвращает
# sorted_nums = sorted(numbers)   # создаёт НОВЫЙ список, оригинал не трогает

#Section 4 - FOR

# for ИМЯ in КОЛЛЕКЦИЯ:
#     что_делать_с_ИМЯ

# Эксперимент 4: первый цикл
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
#
# #Эксперимент 5: цикл с операциями
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(f"I love {fruit}!")
#     print(f"Length: {len(fruit)}")
#     print("---")
#
# #Эксперимент 6: цикл по строке
# word = "Python"
# for letter in word:
#     print(letter)

# #Эксперимент 7: цикл по числам через range()
# for i in range(5):
#     print(i)
#
# for i in range(2, 8):
#     print(i)
#
# for i in range(0, 10, 2):
#     print(i)

# ✅ for fruit in fruits — fruit это новая переменная, которая по очереди принимает каждое значение
# ✅ Цикл по строке — каждый символ отдельно
# ✅ range(5) → 0, 1, 2, 3, 4 (5 не включается!)
# ✅ range(2, 8) → 2-7
# ✅ range(0, 10, 2) → чётные 0,2,4,6,8
# range(N) идёт до N, но не включает N. Это типичный баг — в реальном коде постоянно.
# Например, range(len(list)) — пробежит индексы от 0 до len-1, что и нужно.

#Самые полезные паттерны циклов
#
# #Паттерн 1: enumerate — итерация с индексом
# fruits = ["apple", "banana", "cherry"]
# for i, fruit in enumerate(fruits):
#     print(f"{i}: {fruit}")
#
# # enumerate — встроенная функция, возвращает пары (индекс, значение).
# # Распаковываем в две переменные i, fruit.
#
# ##Паттерн 2: накопление результата
# numbers = [1, 2, 3, 4, 5]
# total = 0
# for n in numbers:
#     total = total + n
# print(total)
#
# #Паттерн 3: фильтрация
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = []
# for n in numbers:
#     if n % 2 == 0:
#         even_numbers.append(n)
# print(even_numbers)
#
# #Паттерн 4: преобразование
# words = ["hello", "world", "python"]
# upper_words = []
# for word in words:
#     upper_words.append(word.upper())
# print(upper_words)

#ЧАСТЬ 3: Цикл while + break/continue
#for — для перебора известной коллекции. Когда знаешь "пройти по всем элементам".
#while — для перебора пока выполняется условие. Когда не знаешь сколько итераций будет.

# Section 5: while loops
# count = 0
# while count < 5:
#     print(f"count is {count}")
#     count = count + 1
# print("done!")

# внутри цикла обязательно что-то меняет условие.
# Если бы не было count = count + 1 — count остался бы 0 навсегда → бесконечный цикл, программа зависнет.

#break — выйти из цикла досрочно
# numbers = [1, 5, 3, 8, 2, 9, 4]
# for n in numbers:
#     if n > 7:
#         print(f"Found big number: {n}")
#         break
#     print(f"Checking {n}")

#continue — пропустить итерацию

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for n in numbers:
#     if n % 2 == 0:
#         continue
#     print(n)

# Когда использовать что
#for — самый частый. 95% случаев.

#"пройти по списку и что-то сделать"
#"повторить N раз через range"

#while — реже. Когда не знаешь количество.

#"ждать пока пользователь не введёт 'exit'"
#"обрабатывать очередь пока она не пуста"

#break — когда нашёл нужное и можно выходить.
#continue — когда хочешь пропустить определённые элементы.

# ЧАСТЬ 4: List Comprehensions
# upper_words = []
# for word in words:
#     upper_words.append(word.upper())

#это равно этому же
# upper_words = [word.upper() for word in words]

# Синтаксис: [ВЫРАЖЕНИЕ for ИМЯ in КОЛЛЕКЦИЯ]
# Читается: "Список из ВЫРАЖЕНИЕ, для каждого ИМЯ в КОЛЛЕКЦИИ".э

# Section 6: list comprehensions
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)

numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)

names = ["Danil", "Anna", "Bob"]
greetings = [f"Hi, {name}!" for name in names]
print(greetings)

#С условием — фильтрация в одну строку
# Old way:
# even = []
# for n in numbers:
#     if n % 2 == 0:
#         even.append(n)
#
# # Comprehension way:
# even = [n for n in numbers if n % 2 == 0]

#Синтаксис: [ВЫРАЖЕНИЕ for ИМЯ in КОЛЛЕКЦИЯ if УСЛОВИЕ]
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = [n for n in numbers if n % 2 == 0]
# print(evens)
#
# big = [n for n in numbers if n > 5]
# print(big)
#
# words = ["apple", "banana", "kiwi", "cherry"]
# short = [w for w in words if len(w) < 6]
# print(short)
# Напиши функцию count_vowels(text),
# которая считает количество гласных букв в строке.
#
# Гласные: a, e, i, o, u (английские, регистр не важен).

# def count_vowels(text):
#     letter = {"a", "e", "i", "o", "u"}
#     result = {}
#     for i in letter:
#         result[i] = text.count(i)
#     a = count.result
#     return result
# print(count_vowels("Hello World"))

def count_vowels_second(text):
    clean_text = text.lower()
    vowels = {"a", "e", "i", "o", "u"}
    count = 0
    for i in clean_text:
        if i in vowels:
            count += 1
    return count

print(count_vowels_second("Hello World"))  # → 3
print(count_vowels_second("Python"))       # → 1
print(count_vowels_second(""))             # → 0
print(count_vowels_second("RHYTHM"))       # → 0

def filter_long_words(words, min_length):
    result = []
    for word in words:
        if len(word) >= min_length:
            result.append(word)
    return result
print(filter_long_words(["Python", "RHYTHM", "ab"], 3))

def word_frequency(words):
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result

print(word_frequency(["python"]))   # {'python': 1}
print(word_frequency([]))           # {}
print(word_frequency(["a", "b", "a", "b", "a"]))  # {'a': 3, 'b': 2}
# Day 3: Strings in Python

# ============================================
# Section 1: String basics
# ============================================
word = "Python"
print(word[0])        # P
print(word[-1])       # n
print(word[1:4])      # yth
print(word[::-1])     # reverse


# ============================================
# Section 2: String methods
# ============================================
word = "J" + word[::-1]
print(word)
text = "Python"
name = "ne_pishi_zdes"
print(text.upper())   # PYTHON
print(text.lower())   # python
print(text.title())   # Python
print(name.title())   # Ne_Pishi_Zdes

print(" hello ".strip()) # hello
print(" hello 1".lstrip()) # "hello "
print(" hello ".rstrip()) # " hello"

print(" hello world".replace("world", "Python")) # Hello Python
print("banana".replace("a", "X")) # bxnxnx
print("banana".replace("a", "X", 1))

print("hello.com".startswith("hello")) # True
print("hello.com".endswith(".com")) # True
print("Hello123".isalnum()) # True
print("Hello 123".isalnum()) # False

text = "Python is cool"
print(len(text)) # 14

# ============================================
# Section 3: F-strings
# ============================================

name = 'Danil'
age = 22
print(f"Hello, {name}!")
print(f"You are {age} years old")
print(f"Next year you will be {age + 1} years old")

pi = 3.14159265
print(f"Pi is {pi}")
print(f"Pi is {pi:.2f}")
print(f"Pi is {pi:.4f}")

percent = 0.85
print(f"Score: {percent:.0%}")

name = "Danil"
score = 87
report = f"""
Name: {name}
Score: {score}
Grade: {"Pass" if score >= 60 else "Fail"}
"""
print(report)
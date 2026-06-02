age = 20

if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Важная деталь про порядок — elif проверяется только если предыдущее не сработало.
# Поэтому условия идут от частного к общему. Если перепутать порядок — логика сломается.

age = 10

if age < 65:
    print("Adult")
elif age < 18:
    print("Minor")

# Условия можно комбинировать через and / or / not:
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")

if age < 16 or age > 70:
    print("Special rules")

# and — оба условия должны быть True
# or — хотя бы одно True
# not — переворачивает

def can_vote(age, is_citizen):
    if age >= 18 and is_citizen:
        return True
    else:
        return False
print(can_vote(20, True))
print(can_vote(10, False))
print(can_vote(10, True))
print(can_vote(18, True))

# *args — функция принимает любое количество позиционных
# аргументов, собирает их в кортеж:

def total(*args):
    print(args)        # это кортеж
    return sum(args)

print(total(1, 2, 3))        # args = (1, 2, 3)
print(total(10, 20, 30, 40)) # args = (10, 20, 30, 40)

# Теперь **kwargs — то же самое, но для именованных
# аргументов, собирает их в словарь:

def make_user(**kwargs):
    print(kwargs)        # это словарь
    return kwargs

make_user(name="Danil", age=25, city="Moscow")
# {'name': 'Danil', 'age': 25, 'city': 'Moscow'}

# Часто их используют вместе, и порядок строгий:
# сначала обычные параметры, потом *args, потом **kwargs:

def log_event(event, *args, **kwargs):
    print(f"Event: {event}")
    print(f"Extra args: {args}")
    print(f"Details: {kwargs}")

log_event("login", "user123", "ip1.2.3.4", status="ok", duration=0.3)

def send_request(method, url, **kwargs):
    # kwargs может быть headers=..., params=..., json=...
    print(f"{method} {url} with {kwargs}")

send_request("GET", "/users", headers={"Auth": "token"}, params={"id": 5})

def build_test_report(suite_name, *results, **meta):
    total = len(results)
    passed = results.count("pass")
    build_result = {
        "suite": suite_name,
        "passed": passed,
        "total": total,
        "meta": meta
    }
    return build_result
print(build_test_report("login_tests", "pass", "fail", "pass", browser="chrome", env="staging"))

# Задачка на if/elif/else + чуть посложнее логика.
# Напиши grade_score(score) которая по баллу возвращает оценку:
#
# 90–100 → "A"
# 80–89 → "B"
# 70–79 → "C"
# меньше 70 → "F"
# а если score вне диапазона 0–100 (например 150 или -5) → "Invalid"

def grade_score(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score <=89:
        return "B"
    elif score >= 70 and score <=79:
        return "C"
    elif score >= 0 and score <=69:
        return "F"
    else:
        return "Invalid"

# print(grade_score(95))   # A
# print(grade_score(85))   # B
# print(grade_score(72))   # C
# print(grade_score(50))   # F
# print(grade_score(150))  # Invalid
# print(grade_score(-5))   # Invalid

def grade_score(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 0 <= score <= 69:
        return "F"
    else:
        return "Invalid"

print(grade_score(95))   # A
print(grade_score(85))   # B
print(grade_score(72))   # C
print(grade_score(50))   # F
print(grade_score(150))  # Invalid
print(grade_score(-5))   # Invalid

# Напиши check_passwords(*passwords) которая принимает
# сколько угодно паролей и возвращает словарь — каждый пароль
# и его статус "strong" или "weak".
# Пароль strong если: длина ≥ 8 и есть хотя бы одна цифра.

def check_passwords(*passwords):
    result = {}
    for password in passwords:
        if len(password) >= 8 and any(char.isdigit() for char in password):
            result[password] = "strong"
        else:
            result[password] = "weak"
    return result
print(check_passwords("abc", "password123", "qwerty"))
print(check_passwords("abcdefgh", "abcdefg1"))
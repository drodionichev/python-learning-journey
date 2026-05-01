# Напиши функцию is_image(filename), которая принимает
# имя файла (строку) и возвращает True, если это картинка (.png, .jpg, .jpeg), и False иначе.

#def is_image(filename):
    #return filename.lower().endswith((".jpg", ".jpeg", ".png"))
#print(is_image("photo.png"))
#print(is_image("IMG.PNG"))
#print(is_image("document.pdf"))
#print(is_image("video.mp4"))
#print(is_image("image.JPEG"))
#print(is_image("script.py"))

# Напиши функцию is_valid_email(email),
# которая принимает строку и возвращает True, если она похожа на email, и False иначе.

# def is_valid_email(email):
#     if " " in email:
#         return False
#     if email.count('@') != 1:
#         return False
#     if len(email.split("@")[0]) == 0:
#         return False
#     if "." not in email.split("@")[1]:
#         return False
#     if len(email.split("@")[1]) <= 2:
#         return False
#     else:
#         return True
# print(is_valid_email("danil@gmail.com"))
# print(is_valid_email("a@b.c"))
# print(is_valid_email("danil@@gmail.com"))
# print(is_valid_email("danil.gmail.com"))
# print(is_valid_email("@gmail.com"))
# print(is_valid_email("danil@gmail"))
# print(is_valid_email("danil @gmail.com"))
# print(is_valid_email(""))
# 2 версия кода
# def is_valid_email(email):
#     if not isinstance(email, str): #проверяем, что приходит строка
#         return False
#     if email.count("@") != 1: # проверяем, что @ только одна
#         return False
#     if " " in email: # проверка, что пробелов не может быть
#         return False
#     name, domain = email.split("@") # разбиваем на части
#     return all([ # в этой функции все тру
#         len(name) >= 1, # длина имени больше 1
#         "." in domain, # в домене есть точка
#         len(domain) >=3 # в домене равно или больше 3 знаков
#     ])
# print(is_valid_email("danil@gmail.com"))
# print(is_valid_email("a@b.c"))
# print(is_valid_email("danil@@gmail.com"))
# print(is_valid_email("danil.gmail.com"))
# print(is_valid_email("@gmail.com"))
# print(is_valid_email("danil@gmail"))
# print(is_valid_email("danil @gmail.com"))
# print(is_valid_email(""))

# user = {"name": "Danil", "age": 22}
# print(user)
# print(user["name"])
# print(user["age"])

# def parse_user (csv_line):
#     part = csv_line.split(",")
#     user = {
#         "name":part[0],
#         "age":int(part[1]),
#         "city":part[2],
#         "email":part[3]
#     }
#     return user
# print(parse_user("Danil,22,Moscow,danil@gmail.com"))

#Напиши функцию build_url(domain, *paths), которая собирает URL из домена и пути.

def build_url(domain, *paths):
    if not paths:
        return domain
    return domain + "/" + "/".join([*paths])
print(build_url("https://example.com", "users", "danil", "profile"))
# должно: "https://example.com/users/danil/profile"

print(build_url("https://api.github.com", "repos", "drodionichev"))
# должно: "https://api.github.com/repos/drodionichev"

print(build_url("https://example.com"))
# должно: "https://example.com"
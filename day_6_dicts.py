# user = {
#     "name": "Danil",
#     "age": 25,
#     "city": "Moscow"
# }
#
# user.keys()    # все ключи
# user.values()  # все значения
# user.items()   # пары (ключ, значение)
#
# for key, value in user.items():
#     print(f"{key}: {value}")
#
# # .update() — обновить/добавить несколько ключей сразу
# user.update({"age": 26, "job": "QA"})
# print(user)
#
# # .pop(key) — удалить ключ и вернуть значение
# city = user.pop("city")
# print(city)   # Moscow
# print(user)   # city уже нет

users = {
    "user_1": {
        "name": "Danil",
        "age": 25,
        "skills": ["Python", "Git"]
    },
    "user_2": {
        "name": "Alex",
        "age": 30,
        "skills": ["Java", "SQL", "Python"]
    }
}
#
# # Доступ к вложенным данным
# print(users["user_1"]["name"])        # Danil
# print(users["user_2"]["skills"])   # Java

def get_skill_summary(users):
    for key, value in users.items():
        print(f"{value['name']}: {', '.join(value['skills'])}")

get_skill_summary(users)

def count_skills(users):
    result = {}
    for key, value in users.items():
        for skill in value["skills"]:  # вот тут идём по скиллам
           result[skill] = result.get(skill, 0) + 1 # тут паттерн счётчика
    return result

print(count_skills(users))

def merge_users(users1, users2):
    result = {}
    result.update(users1)
    result.update(users2)
    return result

print(merge_users(users, users))
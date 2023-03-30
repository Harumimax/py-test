from user.utils.is_user_exist import is_user_exist
from user.user import User

list_of_users = []

hello = input("Хотите выполнить команду? (yes/no) ")
if hello == "no":
    print("Пока пес!")

while(hello == "yes"):
    command = input("Ведите команду (/login, /register, /all_users) ")

    if (command == "/login"):
        continue
    elif (command == "/reg"):
        new_login = input("Введите новый логин ")
        new_pass = input("Введите новый пароль ")
        if is_user_exist(new_login, list_of_users) == True:
            print("Пользователь уже есть")
        else:
            new_user = User(new_login, new_pass)
            list_of_users.append(new_user)
            print("Юзер добавлен")
    elif (command == "/all_users"):
        continue
    else:
        print("команда не правильная")

    hello = input("Хотите выполнить команду? (yes/no) ")
    if hello == "no":
        print("Пока пес!")

print(list_of_users)
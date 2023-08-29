import getpass
import string

# Зарегистрированные пользователи и пароли
registered_users = {
    "user1": "pass1",
    "user2": "pass2",
    "user3": "pass3"
}

while True:
    try:
        username = input("Введите имя пользователя: ")
        if not username:
            raise RuntimeError("Имя не может быть пустым")

        password = getpass.getpass("Введите пароль: ")

        if username in registered_users:
            if password == registered_users[username]:
                print("Доступ разрешен")
            else:
                print("Неверный пароль")
        else:
            print("Пользователь не найден")

        if any(char in string.punctuation for char in password):
            change_password = input("Пароль содержит недопустимые символы. Хотите изменить пароль? (y/n): ")
            if change_password.lower() == "y":
                new_password = input("Введите новый пароль: ")
                registered_users[username] = new_password
                print("Пароль успешно изменен")

        break  # Выход из цикла
    except KeyError:
        print("Пользователь не найден")
    except RuntimeError as e:
        print(e)


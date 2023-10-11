def is_valid_password(password: str) -> bool:

    if len(password) != 8:
        return False

    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_num = True

    return has_upper and has_lower and has_num

    ###   --- OLD VARIANT ---   ###
    # if len(password) != 8:
    #     return False
    
    # flag = False

    # # check for at least one letter in uppercase
    # for item in password:
    #     if item >= 'A' and item <= 'Z':
    #         flag = True
    #         break

    # if not flag:
    #     return False
    # else:
    #     flag = False

    # # check for at least one letter in lower case
    # for item in password:
    #     if item >= 'a' and item <= 'z':
    #         flag = True
    #         break

    # if not flag:
    #     return False
    # else:
    #     flag = False

    # # check for at least one digit
    # for item in password:
    #     if item >= '0' and item <= '9':
    #         flag = True
    #         break

    # if not flag:
    #     return False
    # else:
    #     return True


print(is_valid_password('Qweeee3!'))



'''
Другий етап. Необхідно написати функцію is_valid_password, яка перевірятиме отриманий параметр — пароль на надійність.

Критерії надійного пароля:

Довжина рядка пароля вісім символів.
Містить хоча б одну літеру у верхньому регістрі.
Містить хоча б одну літеру у нижньому регістрі.
Містить хоча б одну цифру.
Функція is_valid_password повинна повернути True, якщо переданий параметр пароль відповідає вимогам на надійність. Інакше повернути False.
'''
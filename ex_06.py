def split_list(grade: list) -> tuple:

    if len(grade) == 0:
        return ([], [])

    s = 0
    list_1 = []
    list_2 = []

    for item in grade:
        s += item
    
    s = s // len(grade)

    for item in grade:
        if item <= s:
            list_1.append(item)
        else:
            list_2.append(item)
        
    return (list_1, list_2)
    

list_main = [80, 96, 45, 96, 99, 74, 26, 76, 88, 92, 45, 65, 67, 89]
# list_main = []

print(split_list(list_main))



'''
У нас є список показників студентів групи – це список з отриманими балами з тестування.
Необхідно поділити список на дві частини. Напишіть функцію split_list, яка приймає список (цілі числа),
знаходить середнє значення бала у списку та ділить його на два списки.
У перший потрапляють значення менше середнього, включаючи середнє значення,
тоді як у другий — строго більше від середнього.
Функція повертає кортеж цих двох списків. Для порожнього списку повертаємо два порожні списки.
'''
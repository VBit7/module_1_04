def amount_payment(payment):

    pay_sum = 0
    for pay in payment:
        if pay > 0:
            pay_sum += pay

    return pay_sum


print(amount_payment([1, 3, 4, -3, 7]))



'''
У нас є список показань заборгованостей з комунальних послуг наприкінці місяця. Заборгованості можуть бути від'ємними — у нас переплата, чи додатними, якщо необхідно сплатити за рахунками. Напишіть функцію amount_payment, яка приймає на вхід список платежів, підсумовує додатні значення та повертає суму платежу наприкінці місяця.
'''
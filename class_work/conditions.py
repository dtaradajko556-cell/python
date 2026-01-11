# print("Hello, world")
# print(10)
# print(10, 12, 14)
# print(10, 5, 6, 6 ,sep=', ')
# # Тип даних - характеристика даних, яка визначає діапазон значень та набір доступних операцій.
# # str - послідовність символів
# # int - цілі числа
# # float - дробові числа
# print(type(10 / 5))
# # Змінна - іменована область пам'яті, що зберігає значення певного типу і може його змінювати
# # протягом виконання програми.
# group = 'П511'
# print(type(group))
# group = 511
# print(type(group))
# weather = input('Введіть поточну погоду: ')
# print(weather)

 
# number1 = float(input("Введіть число: "))
# print(type(number1))
# number2 = float(input("Введіть число: "))
# print(f'{number1} ** {number2} = {number1 ** number2}')
 
#  can_pinguins_swim = True
# can_pinguins_fly = False

# print(f'Чи можуть пінгвіни плавати? {can_pinguins_swim}')
# print(f'Чи можуть пінгвіни літати? {can_pinguins_fly}')
# print(type(can_pinguins_fly))
# print(type(can_pinguins_swim))

# number = int(input("Введіть ціле число: "))

# print(f'{number} > 10? {number > 10}')
# print(f'{number} >= 10? {number >= 10}')
# print(f'{number} < 10? {number < 10}')
# print(f'{number} <= 10? {number <= 10}')
# print(f'{number} == 10? {number == 10}')
# print(f'{number} != 10? {number != 10}')

# is_raining = input("Чи іде зараз дощ? (так/ні) ")

# if is_raining == 'так':
#     print("Беремо парасолю!")

# is_cold = input("Чи зараз холодно? (так/ні)")

# if is_cold == 'так':
#     print('Вдягаємо теплий одяг')
# else:
#     print('Вдягаємо легкий одяг')

# print('Виходимо на вулицю!')
# is_raining = input("Чи іде зараз дощ? (так/ні) ")

# if is_raining == 'так':
#     print("Беремо парасолю!")

'''
# is_cold = input("Чи зараз холодно? (так/ні)")

# if is_cold == 'так':
#     print('Вдягаємо теплий одяг')
# else:
#     print('Вдягаємо легкий одяг')
'''

# temperature = int(input("Скільки зараз градусів на вулиці? "))

# if temperature <= -10:
#     print('Вдягаємось дуже тепло: рукавички, термобілизна, зимова шуба, зимові штанці, черевики')
# elif temperature > -10 and temperature <= 5: # else if
#     print('Вдягаємо тепло: куртка, теплі штанці, теплі кросівки')
# elif temperature > 5 and temperature <= 16:
#     print('Вдягаємось легко: кофта, сорочка, кеди, легкі штанці')
# else:
#     print("Вдягаємось по-літньому: футболка, шорти, шкльопки і на море!")

# print('Виходимо на вулицю!')
# boolean = bool(0) # False

# print(bool(0)) # False
# print(bool(0.0)) # False
# print(bool('')) # False

# something = None
# print(bool(something)) #

# print(bool(10)) # True
# print(bool(-6.8)) # True
# print(bool('hello')) # True

# Калькулятор. Користувач вводить два числа та обирає операцію (+ - * /). Програма виводить результат.
# number1 = float(input("Введіть перше число: "))
# number2 = float(input("Введіть друге число: "))

# operation = input('Оберіть операцію (+, -, *, /): ')

# if operation == '+':
#     print(f'{number1} + {number2} = {number1 + number2}')
# elif operation == '-':
#     print(f'{number1} - {number2} = {number1 - number2}')
# elif operation == '*':
#     print(f'{number1} * {number2} = {number1 * number2}')
# elif operation == '/':
#     if number2 == 0:
#         print('Не можна ділити на нуль!')
#     else:
#         print(f'{number1} / {number2} = {number1 / number2}')
# else:
#     print('Некоректна операція!')

# 1.task# number = int(input('Введите число:'))

# if number % 2 == 0:
#     print(number, 'Even number')
# else:
#     print(number , 'Odd number')
# number = int(input("Введите число: "))

# 2.task# if number % 7 == 0:
#     print(number, "Number is multiple 7")
# else:
#     print(number, "Number is not multiple 7")
# # a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))

# if a > b:
#     print("Max:", a)
# else:
#     print("Max:", b)
# 4.task# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))

# if a < b:
#     print("Min:", a)
# else:
#     print("Min:", b)
# Калькулятор. Користувач вводить два числа та обирає операцію (+ - * /). Програма виводить результат.
# 5.task number1 = float(input("Введіть перше число: "))
# number2 = float(input("Введіть друге число: "))

# operation = input('Оберіть операцію (+, -, *, /): ')

# if operation == '+':
#     print(f'{number1} + {number2} = {number1 + number2}')
# elif operation == '-':
#     print(f'{number1} - {number2} = {number1 - number2}')
# elif operation == '*':
#     print(f'{number1} * {number2} = {number1 * number2}')
# elif operation == '/':
#     if number2 == 0:
#         print('Не можна ділити на нуль!')
#     else:
#         print(f'{number1} / {number2} = {number1 / number2}')
# else:
#     print('Некоректна операція!')


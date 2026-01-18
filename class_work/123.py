# score = int(input("Введіть бал за іспит (0–100): "))

# if score < 0 or score > 100:
#     print("Помилка: бал має бути від 0 до 100")
# elif score >= 90:
#     print("Відмінно")
# elif score >= 70:
#     print("Добре")
# elif score >= 50:
#     print("Задовільно")
# else:
#     print("Незадовільно")

# zarplata = float(input("Введіть вашу заробітну плату: "))
# stazh = float(input("Введіть ваш стаж роботи в роках: "))

# if stazh < 1:
#     print("Премія не передбачена")
# elif stazh < 3:
#     print("Премія:", zarplata * 0.05)
# elif stazh < 5:
#     print("Премія:", zarplata * 0.10)
# else:
#     print("Премія:", zarplata * 0.15)

# num = int(input("Введіть чотиризначне число: "))

# if num < 1000 or num > 9999:
#     print("Помилка: число не є чотиризначним")
# else:
#     n1 = num // 1000
#     n2 = (num // 100) % 10
#     n3 = (num // 10) % 10
#     n4 = num % 10

#     suma = n1 + n2 + n3 + n4

#     if suma % 2 == 0:
#         print("Сума цифр парна")
#     else:
#         print("Сума цифр непарна")

# num = int(input("Введіть шестизначне число: "))

# if num < 100000 or num > 999999:
#     print("Помилка: число не є шестизначним")
# else:
#     n1 = num // 100000
#     n2 = (num // 10000) % 10
#     n3 = (num // 1000) % 10
#     n4 = (num // 100) % 10
#     n5 = (num // 10) % 10
#     n6 = num % 10

#     sum1 = n1 + n2 + n3
#     sum2 = n4 + n5 + n6

#     if sum1 == sum2:
#         print("Число щасливе")
#     else:
#         print("Число нещасливе")


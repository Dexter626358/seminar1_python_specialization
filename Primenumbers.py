"""Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
 Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
  Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч."""
import math


while True:
    print("Введите число: ")
    str_number = input()
    if str_number.isdigit():
        number = int(str_number)
        if number <= 100_000:
            break
        else:
            print("Число не должно быть больше 100000")
    else:
        print("Введены данные, которые не соответствуют условию")
flag = True
if number < 2:
    flag = False
for i in range(2, int(math.sqrt(number)+1)):
    if number % i == 0:
        flag = False
if flag:
    print(f"Число {number} является простым")
else:
    print(f"Число {number} является составным")




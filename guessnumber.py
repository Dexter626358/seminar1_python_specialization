"""Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать «больше» или «меньше» после каждой попытки."""
import random

count = 0
max_attempt = 10
min_number = 0
max_number = 1001
guessed_number = random.randint(min_number, max_number)
winner = False
print(f"Это игра угадайка. Программа загадывает число, а Ваша задача угадать его с {max_attempt} попыток")
while count != max_attempt:
    while True:
        print("Введите число: ")
        str_number = input()
        if str_number.isdigit():
            number = int(str_number)
            break
        else:
            print("Вы ввели не число")
    if number == guessed_number:
        winner = True
        break
    else:
        print("Не верно")
        if guessed_number > number:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")
        count += 1
        print(f"Осталось {max_attempt - count} попыток")

if winner:
    print(f"Вы угадали число с {count} попыток.")
else:
    print(f"Вы проиграли. Загаданное число было: {guessed_number}")



"""Написать программу, которая будет выводить в консоль ёлочку заданной высоты"""

gap = " "
print("Введите высоту елочки")
while True:
    str_height = input()
    if str_height.isdigit():
        height = int(str_height) + 1
        break
    else:
        print("Введите число")
length_gaps = height - 1
length_asterix = 1
for i in range(1, height + 1):
    print(gap * length_gaps, "*" * length_asterix)
    length_gaps -= 1
    if i % 2 == 0:
        length_asterix += 1
    else:
        length_asterix += 2





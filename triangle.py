"""Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
 Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
 Отдельно сообщить является ли треугольник разносторонним,  равнобедренным или равносторонним."""
import random

for i in range(1, 10):
    side_A = random.randint(1, 100)
    side_B = random.randint(1, 100)
    side_C = random.randint(1, 100)
    if (side_A + side_B) > side_C and (side_B + side_C) > side_A and (side_C + side_A) > side_B:
        print(f"Треугольник со сторонами {side_A}, {side_B}, {side_C} существует")
        if side_A == side_B == side_C:
            print("и является равносторонним\n")
        if side_A == side_B != side_C or side_B == side_C != side_A or side_C == side_A != side_B:
            print("и является равнобедренным\n")
    else:
        print(f"Треугольник со сторонами {side_A}, {side_B}, {side_C} не существует")

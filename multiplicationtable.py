"""Написать порграмму, которая выодит в консоль таблицу умножения 'как на тетрадках'"""
print("\t\t\t\t\t\t\tТАБЛИЦА УМНОЖЕНИЯ")
for i in range(1, 9, 4):
    for j in range(1, 11):
        print(f"{i+1} * {j} = {i+1 * j}\t\t\t{i+2} * {j} = {(i+2) * j}\t\t\t{i+3} * {j} = {(i+3) * j}\t\t\t{i+4} * {j} = {(i+4) * j}\t\t\t")
    print("\t")




# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input("Введите число N: "))
list_a = []
for i in range(n):
    list_a.append(int(input("Введите число: ")))
print(list_a)
ai = list_a[i]
x = int(input("Введите число Х: "))
for i in range(n):
    if list_a[i] <= x:
        if ai < list_a[i]:
            ai = list_a[i]
    if list_a[i] >= x:
        if ai > list_a[i]:
            ai = list_a[i]
    if i == n - 1:
        print(ai)
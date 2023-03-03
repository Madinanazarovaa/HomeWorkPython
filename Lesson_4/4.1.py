# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
import random

def fillList(a, list_a):
    for i in range(a):
        list_a.append(random.randint(0, 10))
    print(list_a)

n, m = int(input()), int(input())
list_1, list_2 = [], []
fillList(n, list_1), fillList(m, list_2)
list_3 = list(set(list_1 + list_2))
list_3.sort(reverse=True)
print(list_3)
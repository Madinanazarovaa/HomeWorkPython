# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть

n = int(input("Введите колличество монет: "))
result = 0
for i in range(n):
    a = int(input("Введите 0 или 1: "))
    if a == 1:
        result +=1
        n -= a
if result < n:
    print(f"Мининимальное число монет верх решкой {result}шт.")
else:
    print(f"Минимальное число монет верх гербом {n}шт.")


# Найдите сумму цифр трехзначного числа.

n = int(input("Введите трехзначное число: "))
sum = 0
while n > 0:
    x = n % 10
    sum = sum + x
    n = n // 10
print(sum)
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = int(input('Input number: '))
sum = 0
while number!=0:
    sum += number % 10
    number //=10
print(sum)
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input('Введите число   '))
# res = [1]
# count = 1
# for i in range(1, n):
#     count *= i + 1
#     res.append(count)

res = [i*i for i in range(1, n+1)]

print(res)

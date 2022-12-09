# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.


n = int(input('Введите число   '))
# res = []
# sum = 0

# for i in range(1, n + 1):
#     res.append((1+1/i)**i)
#     sum += (1+1/i)**i
# print(res)
# print(f'Сумма чисел -',sum)

print([(1+1/i)**i for i in range(1, n + 1)])

print('Сумма чисел -', sum([(1+1/i)**i for i in range(1, n + 1)]))

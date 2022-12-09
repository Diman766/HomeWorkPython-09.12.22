# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

lst = [1.1, 1.2, 3.1, 5, 10.01]
# for i in range(0, len(lst)-1):
#     if type(lst[i]) == int:
#         lst.pop(i)

# lst = list(map(str, lst))

lst = list(map(str, filter(lambda x: type(x) == float, lst)))

# lstResult = []

# for i in range(0, len(lst)):
#     tmp = lst[i].split('.')
#     lstResult.append((tmp[1]))

lst = list(map(lambda x: x[1], (map(lambda x: x.split('.'), lst))))

# lstResult = ['0.' + lstResult[i] for i in range(0, len(lstResult))]
# lstResult = list(map(float, lstResult))

lst = ['0.' + i for i in lst]
lst = list(map(float, lst))

print(max(lst) - min(lst))

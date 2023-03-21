# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит
# сами элементы множеств.

i = int(input('ввндите к-во эл-ов 1-го списка: '))
j = int(input('ввндите к-во эл-ов 2-го списка: '))

list1 = []
list2 = []

for k in range(i):
    list1.append(int(input(f'введите {k} элемент 1-го списка: ')))

for k in range(j):
    list2.append(int(input(f'введите {k} элемент 2-го списка: ')))

list1 = set(list1)
list2 = set(list2)

print(list1)
print(list2)
print(sorted(list1.intersection(list2)))

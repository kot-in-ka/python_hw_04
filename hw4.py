# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5
def task1():
    N = int(input("Ищем простые множители числа: "))
    def finding_multiplier(N):
        i = list()
        k = 2
        while k <= N:
            if (N % k) == 0:
                i.append(k)
                N = N / k
            else:
                k += 1
        return i
    print(f"Число {N} состоит из следующих простых множителей: {finding_multiplier(N)}")
    finding_multiplier(N)

# Задача 2. В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.
# Пример:
# 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
# Ответ. Закончилось: «Бурёнка»
def task2():
    file = open("ice_cream.txt", "r", encoding='utf-8')
    data = file.readlines()
    file.close()
    assortment = set(data[0].replace("\n", "").split(", "))
    on_stock = set(data[1].replace("\n", "").split(", "))
    out_of_stock = assortment.difference(on_stock)
    print (f'Ассортимент мороженного: {assortment}')
    print (f'Мороженое на остатках: {on_stock}')
    print (f'Закончилось мороженное: {str(out_of_stock)}')

# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
# 3 -> 3.142
def task3():
    import math
    prec = int(input('Введитете количество знаков после запятой: '))
    print(round(math.pi,prec))


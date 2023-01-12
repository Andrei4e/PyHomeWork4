# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# import math
# d = input('Введите вещественное число: ')
# amt = int(abs(d.find('.') - len (d)) - 1)
# pi = math.pi
# print (round(pi, amt))

#----------------------------------------------------------------------------------------------------------------------------------
#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('Введите целое число: '))

# def PrimeFactors(n):
#     list = []
#     num = 2
#     while num * num <= n:
#         if n % num == 0:
#             list.append(num)
#             n //= num
#         else:
#             num += 1
#     if n > 1:
#         list.append(n)
#     return list
# print(PrimeFactors(n))

#----------------------------------------------------------------------------------------------------------------------------------
#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# numbers = list(input('Введите почледовательность чисел: '))

# def UniqueNumbers(numbers):
#     listUniqueNumbers = []
#     uniqueNumbers = set(numbers)

#     for num in uniqueNumbers:
#         listUniqueNumbers.append(num)

#     return listUniqueNumbers

# print(UniqueNumbers(numbers))


#----------------------------------------------------------------------------------------------------------------------------------
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def ListRandomCoef(k):
    list = [random.randint(0, 101) for i in range(k+1)]
    return list

def CreatePolynomial(listRandomCoef):
    list = listRandomCoef[::-1]
    wr = ''
    if len(list) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                wr += f'{list[i]}x**{len(list)-i-1}'
                if list[i+1] != 0:
                    wr += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                wr += f'{list[i]}x'
                if list[i+1] != 0:
                    wr += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                wr += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                wr += ' = 0'
    return wr

k = int(input("Введите натуральную степень k = "))
coef = ListRandomCoef(k)
with open('file.txt', 'w') as data:
    data.write(CreatePolynomial(coef))

#----------------------------------------------------------------------------------------------------------------------------------
#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов

# def SumPolynomial(dictPolynomial1, dictPolynomial2):
#     dictSum = {}
#     max = 5
#     for i in range(5, 0, -1):
#         number1 = dictPolynomial1.get(i)
#         number2 = dictPolynomial2.get(i)
#         dictSum[i] = number1 + number2
#     return dictSum

# def ResultPolynomial(dictResult):
#     result = ''
#     for i in dictResult.items():
#         if result == '':
#             if i [1] < 0:
#                 result += ' - ' + str(abs(i[1])) + 'x**' + str(abs(i[0]))
#             elif i[1] > 0:
#                 result += str(abs(i[1])) + 'x**' + str(abs(i[0]))
#         else:
#             if i [1] < 0:
#                 result += ' - ' + str(abs(i[1])) + 'x**' + str(abs(i[0]))
#             elif i[1] > 0:
#                 result += ' + ' + str(abs(i[1])) + 'x**' + str(abs(i[0]))    
#     result += ' = 0'
#     return result        

# with open('file1.txt', 'r') as text:
#     polynomial1 = text.readline()
# with open('file2.txt', 'r') as text:
#     polynomial2 = text.readline()

# polynomial1 = polynomial1.replace(' + ', ' +').replace(' - ', ' -')
# polynomial1 = polynomial1.split()
# polynomial1 = polynomial1[:-2]

# polynomial2 = polynomial2.replace(' + ', ' +').replace(' - ', ' -')
# polynomial2 = polynomial2.split()
# polynomial2 = polynomial2[:-2]

# dictionaryPolynomial1 = {}
# dictionaryPolynomial2 = {}

# for i in range(len(polynomial1)):
#       polynomial1[i] = polynomial1[i].replace('+', '').split('x**')
#       polynomial2[i] = polynomial2[i].replace('+', '').split('x**')
#       dictionaryPolynomial1[int(polynomial1[i][1])] = int(polynomial1[i][0])
#       dictionaryPolynomial2[int(polynomial2[i][1])] = int(polynomial2[i][0])

# with open('file3.txt', 'w') as text:
#     text.writelines(ResultPolynomial(SumPolynomial(dictionaryPolynomial1, dictionaryPolynomial2)))


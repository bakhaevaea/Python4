
import math


def Simpl(n):
    # проверка простое ли число
    for i in range (2, int(n/2)):
        if n % i == 0:
            return False
    return True     


def SimpleMulti(num):
    # Задайте натуральное число N. 
    # Напишите программу, которая составит список простых множителей числа N.
    listMulti = []
    multi = 2
    while num > 1:
        if num % multi == 0 and Simpl(multi):
            listMulti.append(multi)
            num = num / multi
            multi = 2
        else: 
            multi += 1
    if len(listMulti) == 1:
        print("Число не имеет простых делителей")
    else:
        print(listMulti)    


def IceCream():
    # в первой строке файла находится информация об асортименте мороженого ,
    # во второй - информация о том, какое мороженое есть на складе. 
    # Выведите названия того товара, котоый закончился
    data = open("Мороженое.txt", "r", encoding='utf-8')
    text = data.readlines()
    IceCr = set(text[0][:-1].split(","))
    Ost = set(text[1].split(","))
    data.close()
    print(IceCr)
    print(Ost)
    print("Закончилось: ", IceCr-Ost)

def PrintPi():
    # Выведите число Pi с заданной точностью. 
    # Точность вводится пользователем в виде натурального числа
    n = int(input("С какой точностью вывести число Pi?  ")) 
    print(round( math.pi,n))

def ReadMn(file):
    data = open(file, "r")
    MN = data.read()
    data.close()
    
    MN = MN.split()
    for i in range(len(MN)):   # добавляем 1 перед х
        if MN[i][0] == "x":
            MN[i] = "1" + MN[i]
    
    for i in range(len(MN)):    # если знак операции - , меняем знак следущего числа
        if MN[i] == "-":
            MN[i+1] =  "-" + MN[i+1]

    MN = MN[0::2]   # убираем из списка элементы - знаки (+ и -)
    
    for i in range(1,3):    # проверяем 2 последних элемента (они могут быть степени 1 и 0)
        if MN[- i][-1] == "x":
            MN[-i] = MN[-i] + "^1"   # для х дописываем ^1
        elif MN[-i][-1] != "x":
            MN[-i] = MN[-i] + "x^0"   # для просто числа дописываем ^0
    return MN

def MnInList(MN):  # создаем список коэфициентов на местах = степени  х
    listMn = [ 0 for i in range(int(MN[0].split("x^")[1])+1)]
    for i in MN:
        el = i.split("x^")
        listMn[int(el[1])] = el[0]

    return listMn

def PrintMN(file, MN):  # печать многочлена в файл
    Otvet = str(MN[len(MN)-1])+"x^"+ str(len(MN)-1) + " "
    for i in range(len(MN)-2, -1, -1):
        if MN[i] != 0:
            if MN[i]>0: Otvet += "+ "
            if i == 1: Otvet += str(MN[i]) + "x "
            elif i == 0: Otvet += str(MN[i])
            else: Otvet += str(MN[i]) + "x^" + str(i) + " "
    data = open(file, "w")
    data.write(Otvet)
    data.close()


def  PlusMN():
    # Даны 2 файла, в каждом из которых находится запись многочлена.
    # Найдите сумму данных  многочленов
    Mn1 = MnInList( ReadMn("MN1.txt"))
    Mn2 = MnInList( ReadMn("MN2.txt"))

    # для сложения подровняем их под один размер
    for i in range(len(Mn1), max(len(Mn1), len(Mn2))):
        Mn1.append(0)    
    for i in range(len(Mn2), max(len(Mn1), len(Mn2))):
        Mn2.append(0)

    SumMN = [int(Mn1[i]) + int(Mn2[i]) for i in range (max(len(Mn1), len(Mn2)))]
    PrintMN("MN3.txt", SumMN)




# IceCream()
# SimpleMulti(103)
# PrintPi()
PlusMN()

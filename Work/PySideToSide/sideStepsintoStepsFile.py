import os
import shutil
from sys import argv


# Извлечение шагов B-файла в отдельный файл
b = open("B.txt", 'r').read()
StepsB = open("StepsB.txt", 'w')
StepsB.write(b[135:-284])
StepsB.close()

# Извлечение шагов A-файла в отдельный файл
a = open("A.txt", 'r').read()
StepsA = open("StepsA.txt", 'w')
StepsA.write(a[135:-284])
StepsA.close()


# извлечение заголовка А
a = open('A.txt', 'r').read()
head = open('Head.txt', 'w')
head.write(a[:136])
head.close()

# Извлечение нижней части документа A
a = open('A.txt', 'r').read()
flat = open('Flat.txt', 'w')
flat.write(a[-284:])
flat.close()





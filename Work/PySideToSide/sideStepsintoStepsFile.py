import os
import shutil
from sys import argv


# Извлечение шагов B-файла в отдельный файл
b = open("B.txt", 'r').read()
StepsB = open("StepsB.txt", 'w')
cutB = str(b[b.index('"tests"'):b.index('"suites":')])
#отрезать 10 символов слева надо!!

StepsB.write(cutB)
StepsB.close()

# Извлечение шагов A-файла в отдельный файл
a = open("A.txt", 'r').read()
StepsA = open("StepsA.txt", 'w')

cuttingA = str(a[:a.index('"suites"')])
a = str(cuttingA[:-5])

StepsA.write(a)
StepsA.close()


## извлечение заголовка А
#a = open('A.txt', 'r').read()
#head = open('Head.txt', 'w')
#head.write(a[:136])
#head.close()

# Извлечение нижней части документа A
a = open('A.txt', 'r').read()
flat = open('Flat.txt', 'w')
cutFlat = str('"' + a[a.index("suites"):])
flat.write(cutFlat)
flat.close()





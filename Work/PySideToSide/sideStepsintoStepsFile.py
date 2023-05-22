import os
import shutil
from sys import argv


# Извлечение шагов в отдельный файл
b = open("B.txt", 'r').read()
result = open("Steps.txt", 'w')
result.write(b[135:-284])
result.close()

# извлечение заголовка А
a = open('A.txt', 'r').read()
head = open('Head.txt', 'w')
head.write(a[:136])
head.close()

# Извлечение нижней части документа
a = open('A.txt', 'r').read()
flat = open('Flat.txt', 'w')
flat.write(a[-284:])
flat.close()





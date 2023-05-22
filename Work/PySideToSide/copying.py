import os
import shutil
from sys import argv

def StepsAStepsB():
    
    stA = open('StepsA.txt', 'a+')

    stB = open("StepsB.txt", 'r')
    #stB = stB + ']' + ','

    stA.write(stB.read())

    stA.close()
    stB.close()


def StepsAFlat():
    stA = open('StepsA.txt', 'a+')

    flat = open("Flat.txt", 'r')

    stA.write(flat.read())

    stA.close()
    flat.close()

def Main():
    StepsAStepsB()
    StepsAFlat()

Main()
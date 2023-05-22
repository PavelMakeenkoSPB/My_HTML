import os
import shutil
from sys import argv

def HeadStep():
    
    head = open('Head.txt', 'a+')

    steps = open("Steps.txt", 'r')

    head.write(steps.read())

    head.close()
    steps.close()


def HeadFlat():
    head = open('Head.txt', 'a+')

    flat = open("Flat.txt", 'r')

    head.write(flat.read())

    head.close()
    flat.close()

def Main():
    HeadStep()
    HeadFlat()

Main()
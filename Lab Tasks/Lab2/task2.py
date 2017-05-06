import math
x = int(input('Enter the 1st Num'))
y = int(input('Enter the 2nd Num'))
op = input('Enter the operator')

def add(x, y):
    Answer = x + y
    return Answer

def sub(x, y):
    Answer = x - y
    return Answer

def mul(x, y):
    Answer = x * y
    return Answer

def div(x, y):
    Answer = x / y
    return Answer

if (op=="+"):

       print(add(x,y))
if (op=="-"):

       print( sub(x,y))
if (op=="*"):

       print(mul(x,y))
if (op=="/"):

       print(div(x,y))







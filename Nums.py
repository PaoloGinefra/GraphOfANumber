import turtle
import math
import math_pi

Forward = 40
Angle = 10
Steps = 10000

unit = 360 / 10
Num = str(math_pi.pi(b = 1000))

def Devide(a, b):
    digits = []
    rem = 0
    i = 1
    c = a[0]
    length = len(a)
    rem = (10 * rem + int(c)) % b
    while((rem != 0 or i < length) and i < Steps):
        if(i < length):
            c = a[i]
        else:
            c = '0'
        digits.append((10 * rem + int(c)) // b)
        rem = (10 * rem + int(c)) % b

        i += 1

    return digits


dig = Devide(str(5), 119)

s = turtle.getscreen()
t = turtle.Turtle()
t.speed(500)


for d in dig:
    print(d)
    t.forward(Forward)
    t.lt(d * unit)

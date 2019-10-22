from math import sqrt

x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))
x3 = float(input('x3: '))
y3 = float(input('y3: '))
x4 = float(input('x4: '))
y4 = float(input('y4: '))

ab = sqrt((x2 - x1)**2 + (y2 - y1)**2)
bc = sqrt((x3 - x2)**2 + (y3 - y2)**2)
cd = sqrt((x4 - x3)**2 + (y4 - y3)**2)
ad = sqrt((x4 - x1)**2 + (y4 - y1)**2)

d1 = sqrt((x3 - x1)**2 + (y3 - y1)**2)
d2 = sqrt((x2 - x4)**2 + (y2 - y4)**2)

if (ab == cd) and (bc == ad):
    print('Перша діагональ: ' + str(round(d1, 3)))
    print('Друга діагональ: ' + str(round(d2, 3)))

    cosA = (d1**2+d2**2-(4*ab**2))/(2 * d1 * d2)
    sinA = sqrt(1 - cosA**2)
    S = (d1 * d2 * sinA) * (1/2)

    print('Площа паралелограма: ' + str(round(S, 3)))
else:
    print('Не паралелограм ')
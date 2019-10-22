from math import sqrt

print('Перевірити чи належить точка, яка задається своїми трьома координатами, внутрішній області сфери.')
x = float(input('x: '))
y = float(input('y: '))
z = float(input('z: '))

R = float(input('Введіть радіус сфери: '))
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

if (R<sqrt((x-a)**2+(y-b)**2+(z-c)**2)):
    print("Точка знаходиться за межами сфери")
else:
    print("Точка належить внутрішній області сфери")
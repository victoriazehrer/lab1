print('Вивести список всіх дільників числа m.')

m = int(input('Введіть число m: '))
l = [x for x in range(1, m+1 ) if m % x == 0]
print(l)
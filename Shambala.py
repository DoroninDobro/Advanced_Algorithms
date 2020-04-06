'''В данной задаче нужно вывести на экран в символическом виде концентрические круги символами ‘X’ и пробелами, 
количество которых зависят от номера N текущего дня.

На вход подаётся одна строка с числом N [1, 30].

На выход нужно подать несколько строк с изображением шамбалы.
'''

x = int(input())
mass = []
x = x*2-1
for i in range(int(x/2)):
    mass.append('X' * x)
    mass.append(' ' * x)
mass.append('X' * x)
u = 1
d = x-2
l_block = 'X '
r_block = ' X'
for k in range(int(x/4)):
    blocks = k + 1
    y = x - blocks * 4
    str_sp = l_block * blocks + ' ' * y + r_block * blocks
    str_X = l_block * blocks + 'X' * y + r_block * blocks
    mass[u] = str_sp
    mass[d] = str_sp
    mass[u+1] = str_X
    mass[d-1] = str_X 
    u += 2 
    d -= 2
mass[int(x/2)] = 'X ' * int(x/2)+'X' 
for j in mass:
    print(j) 

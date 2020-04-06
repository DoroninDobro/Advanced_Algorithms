'''В лифте есть две кнопки для движения вниз:

спустится вниз на один этаж;

спустится вниз на два этажа.

Если лифт находится на втором этаже, то он может спуститься только на один этаж.

Остановка на каждом этаже имеет стоимость, включая и нахождение на верхнем этаже.
Стоимость может принимать целые значения из диапазона - [0, 50].

Нужно найти минимальную стоимость спуска с верхнего этажа на первый.
'''

f = int(input())
costs = [int(x) for x in input().split()]
m = [3000] * f
local_cost = 0
first_cost = []

def downhill(local_cost, current_floor, m, costs): #7
    if current_floor < 1:
        return 'You are in hell'
    local_cost += costs[current_floor -1]
    if current_floor == 1:
        first_cost.append(local_cost)
        return 'You are in paradise'
    if local_cost <= m[current_floor - 1]: # here wrong!
        m[current_floor - 1] = local_cost
        a = downhill(local_cost, current_floor - 2, m, costs)
        b = downhill(local_cost, current_floor - 1, m, costs)

    
    
ans = downhill(local_cost, f, m, costs)
#print(first_cost)
print(min(first_cost))


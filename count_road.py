'''Прямоугольное поле размерностью N×M заполняется целыми неотрицательными числами. 
Цель состоит в том, чтобы пройти по любому разрешенному пути от верхнего левого угла до правого нижнего. 
Целое число в каждой клетке указывает, какой длины шаг должен быть из текущей клетки. 
Все шаги могут быть или направо, или вниз. Запрещены шаги за пределы поля игры.

Требуется написать программу, которая определит количество различных вариантов путей 
от верхнего левого угла до правого нижнего.
'''

# first solution
a, b = map(int, input().split())
price = []
for _ in range(a):
    price.append([int(j) for j in input().split()])
count = 0
counts = 0
    
def road(row, column):
    global count
    global counts
    counts += 1
    print(row, column)
    if row == a - 1 and column == b - 1:
        count += 1
        #return 'nothing'
    else:
        step = price[row][column]
        if step == 0:
            pass
        else:
            if row + step < a:
                c = road(row+step, column)

            if column + step < b:
                d = road(row, column + step)
e = road(0, 0)
print(counts)








# second solutions
a, b = map(int, input().split())
price = []
for _ in range(a):
    price.append([int(j) for j in input().split()])
costs = [[float('inf')] * b for i in range(a)]
#parents = [[''] * b for i in range(a)]
costs[0][0] = price[0][0]
costs[a-1][b-1] = price[a-1][b-1]
#costs[0][1] = price[0][1] + costs[0][0]
#parents[0][1] += '1'
#costs[1][0] = price[1][0] + costs[0][0]
#parents[1][0] += '0'
processed = [[a-1, b-1]]
countsss = 0
 
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for i in range(len(costs)):
        for h in range(len(costs[i])):
            cost = costs[i][h]
            node = [i, h]
            if cost <= lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
                row = i
                column = h
    if lowest_cost_node == float('inf'):
        return None, 0, 0
    elif lowest_cost_node:
        node = costs[lowest_cost_node[0]][lowest_cost_node[1]]
    else:
        return None, 0, 0
    return node, row, column
    
node, row, column = find_lowest_cost_node(costs)

while node is not None: 
    if row == a-1 and column == b-1:
        countsss += 1
    else:
        step = node
        if row + step < a:
            neigb = price[row+step][column]
            #new_cost = cost + neigb
            #if costs[row+1][column] > new_cost:
            costs[row+step][column] = neigb
            if row + step == a-1 and column == b-1:
                countsss += 1
                #parents[row+1][column] = parents[row][column] + '0'# !
        if column + step < b:
            neigb = price[row][column+step]
            #new_cost = cost + neigb
            #if costs[row][column+1] > new_cost:
            costs[row][column+step] = neigb
            if row == a-1 and column + step == b-1:
                countsss += 1
                #parents[row][column+1] = parents[row][column] + '1'# !
        processed.append([row, column])
        node, row, column = find_lowest_cost_node(costs)
    
print(countsss) 








# third solution
a, b = map(int, input().split())
price = []
for _ in range(a):
    price.append([int(j) for j in input().split()])
    
def count(row, column):
    counts = 0
    if row != 0:
        for i in range(1, row+1):
            if row - i == 0 and column == 0 and price[0][0] == i:
                counts += 1
            elif price[row-i][column] == i:
                counts += count(row-i, column)
    if column != 0:
        for i in range(1, column+1):
            if row == 0 and column - i == 0 and price[0][0] == i:
                counts += 1
            elif price[row][column-i] == i:
                counts += count(row, column-i)
    return counts
print(count(a-1, b-1))



# fourth solution
a, b = map(int, input().split())
price = []
for _ in range(a):
    price.append([int(j) for j in input().split()])
memory = [[float('inf')] * b for i in range(a)]
    
def count(row, column):
    if memory[row][column] != float('inf'):
        return memory[row][column]
    counts = 0
    if row != 0:
        for i in range(1, row+1):
            if row - i == 0 and column == 0 and price[0][0] == i:
                counts += 1
            elif price[row-i][column] == i:
                counts += count(row-i, column)
    if column != 0:
        for i in range(1, column+1):
            if row == 0 and column - i == 0 and price[0][0] == i:
                counts += 1
            elif price[row][column-i] == i:
                counts += count(row, column-i)
    memory[row][column] = counts
    return counts
print(count(a-1, b-1))

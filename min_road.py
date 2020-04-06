'''Символ 0 обозначает движение на один шаг вниз, а
символ 1 - движение на один шаг вправо.
Чтобы исключить множество возможных вариантов минимального 
пути для случаев когда стоит выбор перехода в данную ячейку
из ячейки сверху или слева и оба варианта дают путь одинаковой длины - 
в этих случаях предпочитайте шаг из верхней ячейки вниз. Рассмотрим пример, пусть дана таблица:
1 1 2
1 1 1
2 1 1
Для такой таблицы будет несколько путей минимальной длины (все, которые не проходят через двойки), 
но вы должны будете выбрать путь 0101, который означает "вниз-вправо-вниз-вправо". Всего 4 шага, так как в первой 
(самой левой верхней ячейке игрок находится изначально).
'''

# put your python code here
a, b = map(int, input().split())
price = []
for _ in range(a):
    price.append([int(j) for j in input().split()])
costs = [[float('inf')] * b for i in range(a)]
parents = [[''] * b for i in range(a)]
costs[0][0] = price[0][0]
costs[0][1] = price[0][1] + costs[0][0]
parents[0][1] += '1'
costs[1][0] = price[1][0] + costs[0][0]
parents[1][0] += '0'
processed = [[0,0]]


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
    if lowest_cost_node:
        node = costs[lowest_cost_node[0]][lowest_cost_node[1]]
    else:
        return None, 0, 0
    return node, row, column
    
node, row, column = find_lowest_cost_node(costs)

while node is not None: 
    cost = node
    if row + 1 < a:
        neigb = price[row+1][column]
        new_cost = cost + neigb
        if costs[row+1][column] > new_cost:
            costs[row+1][column] = new_cost
            parents[row+1][column] = parents[row][column] + '0'# !
    if column + 1 < b:
        neigb = price[row][column+1]
        new_cost = cost + neigb
        if costs[row][column+1] > new_cost:
            costs[row][column+1] = new_cost
            parents[row][column+1] = parents[row][column] + '1'# !
    processed.append([row, column])
    node, row, column = find_lowest_cost_node(costs)
    
print(parents[-1][-1]) 

'''На расстоянии n шагов от магазина стоит человек. Каждую секунду он выбирает, куда сделать шаг: 
к магазину или в противоположном направлении. Напишите программу, которая определит, 
сколькими способами он может попасть в магазин, пройдя ровно k шагов и оказавшись в магазине 
только после выполнения последнего шага.

На вход подаются через пробел два целых числа n – расстояние до магазина в шагах и k – требуемое количество шагов, 
которые должен сделать человек (1 ≤ n ≤ k ≤ 50).

На выход следует подать только одно число - количество способов попадания в магазин.
'''

i = input().split()
shop = int(i[0])
count = int(i[1])
memory = []
for _ in range(count):
    memory.append([0]* (count))
def p(count, shop):
    if count == shop:
        return 1
    if count == shop+2:
        return shop
    else:
        b = pp(count, shop)
        return b
    
def pp(count, shop):
    global memory
    #print(count, shop)
    if shop == 0 or shop > count:
        #print('here 0')
        return 0
    if memory[count-1][shop-1] == 0:
    
        if shop == count - 4:
            #print('here umn')
            s = int((shop+3) * (shop/2))
            memory[count-1][shop-1] = s
            return s
        else: 
            s = pp(count-1, shop+1) + pp(count-1, shop-1)
            memory[count-1][shop-1] = s
            return s
    else:
        return memory[count-1][shop-1] 
a = p(count, shop)
print(a)
#print(memory)

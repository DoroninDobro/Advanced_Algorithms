def maxi(m):
    m1 = [i for i in m]
    max1 = max(m1)
    del(m1[m1.index(max1)])
    max2 = max(m1)
    del(m1[m1.index(max2)])
    max3 = max(m1)
    return max1 * max2 * max3
    
def mini(m):
    m1 = [i for i in m]
    min1 = min(m1)
    del(m1[m1.index(min1)])
    min2 = min(m1)
    return min1 * min2 * max(m)

n = int(input())
m = [int(i) for i in input().split()]
minus = [i for i in m if i < 0]
if n == 3 or len(m) == len(minus) or len(minus) < 2:
    print(maxi(m))
else:
    maxim = []
    maxim.append(mini(m))
    maxim.append(maxi(m))
    print(max(maxim)) 

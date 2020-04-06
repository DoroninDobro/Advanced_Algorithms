# Даны целые числа n 1≤n≤10**18 и m 2≤m≤10**5, 
# необходимо найти остаток от деления nn-го числа Фибоначчи на mm.

def fib_mod(n, m):
    period = [0,1]
    f = 0
    fib = [0,1]
    #a, b = 0, 1
    for i in range(2, n+1):
        #a, b = b, a+b
        fib.append((fib[i-1] + fib[i-2])%m)
        period.append(fib[i]%m)
        if period[-2:] == [0,1]:
            f = 1
            period = period[:-2]
            break
    if f== 1:
        return period[n%(len(period))]
    return fib[n]%m



def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()

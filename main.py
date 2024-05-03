#1

def F1(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n > 2:
        return F1(n-1)*n + F1(n-2)*(n-1)



def F3(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return F3(n-1) - F3(n-2) + 2*n


print(F3(6))

def F5(n):
    if n == 1:
        return 1
    if n % 2 != 0 and n > 1:
        return n + F5(n-2)
    if n % 2 == 0:
        return n*F5(n-1)

print(F5(40))

7

def F7(n):
    if n < 3:
        return 1
    if n > 2:
        return sum(F7(i) for i in range (1,n))
print(F7(18))

def F8(n):
    if n >= len(f8_list):
        for i in range(len(f8_list), n + 1):
            f8_list.append(i + F8(i - 1))
    return f8_list[n]
f8_list = [10]*11
print(F8(2021)-F8(2019))

def F9(n):
    if n >= 1000: return 1000
    if n < 1000 and n % 2:
        return n * F9(n + 1)
    else:
        return n * (F9(n + 1) // 2)


print(F9(998) // F9(1001))


def f3(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    else:
        return f3(x + 2, y) + f3(x + 4, y)
#print(f3(4, 22))

def f2(x, y):
   if x > y or x == 17:
       return 0
   if x == y:
       return 1
   return f2(x + 1, y) + f2(x + 2, y) + f2(x * 3, y)
print(f2(3, 10) * f2(10, 25))

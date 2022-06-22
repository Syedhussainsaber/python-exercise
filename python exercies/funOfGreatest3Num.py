def greatestOf3Num(a,b,c):
    if a>b and a>c :
        return a
    elif b>c:
        return b
    else:
        return c
    
n=greatestOf3Num(7,6,5)
print(n)
  
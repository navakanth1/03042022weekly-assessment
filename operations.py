import cmath as m
def Sqrt(a):
    b = m.sqrt(a)
    return b
def Quadratic(a,b,c):
    x = (b*b)-(4*a*c)
    return x
def Degree(a):
    b = (a*(9/5))+32
    return b
def Number(a):
    if a>0:
        return "Positive"
    elif a<0:
        return "Negative"
    else:
        return "0"
def Sum(n):
   if n <= 1:
       return n
   else:
       return n + Sum(n-1)

if __name__=="__main__":
    a = int(input("Enter sqrt number:"))
    b = int(input("Enter  element1:"))
    c = int(input("Enter  element2:"))
    d = int(input("Enter  element3:"))
    e = int(input("Enter Celcius:"))
    f = int(input("Enter number for positive negative zero:"))
    g = int(input("Enter the number for sum:"))
    result1 = Sqrt(a)
    result2 = Quadratic(b,c,d)
    result3 = Degree(e)
    result4 = Number(f)
    result5 = Sum(g)
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
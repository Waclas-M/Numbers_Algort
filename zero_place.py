def f(x):
    return x**2-60

def zero_place(eps):
    a = 0
    b = 10
    while abs(b-a)>eps:
        c=(a+b)/2
        if f(c)>0:
            b=c
        else:
            a=c

    return c

print(round(zero_place(0.001),3))





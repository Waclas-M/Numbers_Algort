def mProstokonrow(a,b,n):
    dx = (b-a)/n
    h=0
    sr=a+(b-a)/(2.0 * n)
    i=0
    while i<n:
        h= h+sr
        sr = sr+dx
        i+=1
    return h*dx

print(mProstokonrow(0,10,10))

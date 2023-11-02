def horner(x,st,list):
    y=list[0]
    for i in range(1,st+1):
        y=y*x+list[i]
    return y

def sqrt(pierwiastek,dokładność):
    bok_a = pierwiastek /2
    bok_b = pierwiastek / bok_a
    boki = bok_a-bok_b
    if boki<0:
        boki=bok_a-bok_b
        boki = boki * -1

    while boki>=dokładność:
        if bok_a*bok_a == pierwiastek:
            return bok_a

        else:
            bok_a = (bok_a+bok_b)/2
            bok_b= pierwiastek / bok_a
            if bok_a<0:
               bok_a = bok_a * -1
        boki = bok_a-bok_b
        if boki == 0:
            return bok_a
    return bok_a



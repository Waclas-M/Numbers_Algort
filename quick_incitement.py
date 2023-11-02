def incitement(liczba_a,n):
    w=1
    while n > 0:
        if n % 2 == 1:
            w=w*liczba_a
        liczba_a = liczba_a * liczba_a
        n=n//2

    return w

print(incitement(8,9))


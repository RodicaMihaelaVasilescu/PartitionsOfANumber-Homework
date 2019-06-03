#modules.py
def partitie(k, s, x, n):
    if s == n:                            #cand suma elementelor listei x este egala cu n
        for j in range (1, k-1):          #afisam elementele listei x
            print(x[j], end=' +')
        print(x[k-1],end=' =')
        print(n)

    else:                                 #bakcktracking:
        for i in range(x[k-1]+1, n-s+1):  #elementele listei vor fi in ordine strict crescatoare
            x[k] = i
            s = s + x[k]                  #in s calculam suma elementelor listei
            partitie(k+1, s, x, n)        #recursivitate
            s = s - x[k]


def invers(nr):                           #inversul unui numar
    inv = 0
    aux = nr
    while aux != 0:
        inv = inv*10 + aux%10
        aux = aux//10

    if inv == nr:
        return 1
    else:
        return 0


def palindrom(n):                        #palindrom

    i = 1
    nr = 0

    while i <= n :                       #cat timp nu am ajuns la al n-lea palindrom
        nr += 1
        if invers(nr) == 1 :             #cautam termeni palindromici
            i += 1

    return  nr

def submultime(k, s, x, n):                          #submultime
    for i in range(x[k-1], s+1 ):                    #backtracking
        x[k] = i
        if x[k] == s:
            for l in range(1, k ):
                print(x[l], end=' +')                 #afisare
            print(x[k])
        else: submultime (k + 1, s - x[k], x, n)      #recursivitate
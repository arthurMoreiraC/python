

def q():
    d = input("digite a direção -1: horario e 1 antihorario: ")
    direcao = int(d)
    h = input("digite a posicao do helicoptero: ")
    helicoptero = int(h)
    p = input("digite a posicao do policial: ")
    policial = int(p)
    f = input("digite a posicao do fugitivo: ")
    f = int(f)

    ended = False

    while not ended:
        f += direcao
        if f <0:
            f = 15
        elif f > 15:
            f = 0

        if f == policial:
            print("N")
            ended = True
        elif f == helicoptero:
            print("S")
            ended = True


    

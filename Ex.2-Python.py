var = "variavel"
sapatos = []
class sapato:
    def __init__(self, M, L):
        self.M = M
        self.L = L

while(var != "EOF"):
    print("Número de botas (deve ser par!): ")
    var = input()
    if(var == "EOF"):
        print("Fim do Arquivo!")
        exit()
    else:
        if(int(var)%2 != 0):
            print("Número de botas deve ser par!")
            exit()
        else:
            for i in range(0, int(var)):
                print("Descrição das botas: ")
                descricao = input()
                M, L = descricao.split(' ', 1)
                M = int(M)
                if(M < 30 or M > 60 or (L != 'E' and L != 'D')):
                    print("Tamanho ou pé inválido")
                    exit()
                sapatos.append(sapato(M, L))
            numpares = 0
            for i in sapatos:
                for j in sapatos:
                    if(i.M == j.M and i.L != j.L):
                        numpares = numpares + 1
                        sapatos.remove(j)
                        break
                sapatos.remove(i)
            print(numpares)
        numpares = 0
        sapatos = []


print("Digite um número: ")
numero = int(input())
lista = []
lista2 = []

for i in range(1, numero + 1):
    lista2.append(i)

for i in range(1, numero):
    print("Lista: ")
    m = int(input())
    lista.append(m)
print(numero)
print(lista)
print(lista2)

for i in lista2:
    if i not in lista:
        print(i)



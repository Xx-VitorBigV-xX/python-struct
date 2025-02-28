#Inicializando lista
lista = []
impar = []
par = []

#Lendo valores
for i in range(2):
    numero = int(input(f"Digite {i+1} número: "))
    lista.append(numero) #adicionando valores na lista
    if numero %2==0: #verificando se numero dividio por 2 é zero
        par.append(numero)  #caso seja adiciona numero na lista de pares
    else:
        impar.append(numero) #Caso não seja adiciona numero na lista de impares



    
print(f"\nLista de números: {lista}")
print(f"Lista de números pares: {par}")
print(f"Lista de números impares: {impar}")
# Inicializando a lista
valorInicial = []
valorNegativo = []

# Inicializando as listas
valorInicial = []
valorNegativo = []

# Lendo 10 valores
for i in range(10):
    valor = int(input(f"Digite {i+1}º número: "))
    valorInicial.append(valor)  # Armazenando valor na lista valorInicial
    
    # Verificando se o valor é negativo
    if valor < 0:
        valorNegativo.append(valor)  # Adicionando o valor negativo à lista valorNegativo

# Removendo os valores negativos da lista valorInicial
valorInicial = [v for v in valorInicial if v >= 0]

# Imprimindo as listas
print("Lista de valores digitados (sem negativos):", valorInicial)
print("Lista de valores negativos:", valorNegativo)

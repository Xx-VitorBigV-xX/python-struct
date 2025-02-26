#Cálculo da área e comprimento da circunfêrencia 
#comprimento = 2 x pi*raio

raio = float(input("digite o valor do raio"))
area = 3.14159 * raio ** 2
comprimento = 2 * 3.14159 * raio
print('Para o raio {},  área = {:.3f} e o comprimento = {}'.format(raio, area, comprimento))



# Calculando a distância entre os pontos (3,4) e (5,6)
x1 = 3
y1 = 4
x2 = 5
y2 = 6
dist = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
print('A distância entre os pontos({},{}) e ({},{}) = {}.'.format(x1, y1, x2, y2, dist))
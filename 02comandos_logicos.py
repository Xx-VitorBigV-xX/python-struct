#Operadorwes racionais 

a,b,c,d  = 10,15,0,-4

print(a==b)
#coloque dentro do print para o valor booleano
a==10
c!=0
d!=b
b>d
b>15
b>=15
c<a

#Operadores lógicos 

#and 
print((c+b<a) and (d<0))
print(c<a)and (a==b)

#or
(c<a)or(a==b)

#NOT
not(c>10)




#IF
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
if x < y:
    print("{} é maior que {}".format(x,y))
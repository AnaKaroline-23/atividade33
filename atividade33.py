#Mostre-me as seguintes listas, derivadas de:
#[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#Intervalo de 1 a 9
#Intervalo de 8 a 13
#Números pares
#Números ímpares
#Todos os múltiplos de 2,3 e 4
#Lista reversa
#Razão entre a soma do intervalo de 10 a 15 pelo intervalo de 3 a 9 em float!
lista_base = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
intervalo_1_9 = []
intervalo_8_13 = []
intervalo_10_15 = []
intervalo_3_9 = []
lista_par = []
lista_impar = []
mult_2 = []
mult_3 = []
mult_4 = []

for item in lista_base:
    if item >=1 and item < 9:
        intervalo_1_9.append(item)

for i in lista_base:
    if i >=8 and i < 13:
        intervalo_8_13.append(i)

print("o intervalo de 1 a 9 é: ",intervalo_1_9)
print("o intervalo de 8 a 13 é: ",intervalo_8_13)

for par in lista_base:
    if par % 2 ==0:
        lista_par.append(par)
    else:
        lista_impar.append(par)

print("a lista com numeros pares é: ",lista_par)
print("a lista com numeros impares é: ",lista_impar)

for item in lista_base:
    if item % 2 == 0 :
        mult_2.append(item)
    
for item in lista_base:
    if item % 3 == 0:
        mult_3.append(item)

for item in lista_base:
    if item % 4 == 0:
        mult_4.append(item)

print("a lista com numeros multiplos de 2 é: ",mult_2)
print("a lista com numeros multiplos de 3 é: ",mult_3)
print("a lista com numeros multiplos de 4 é: ",mult_4)

reverso = lista_base[::-1]
print("a lista reversa é: ",reverso)

for i in lista_base:
    if i >=10 and i < 16:
        intervalo_10_15.append(i)

for i in lista_base:
    if i >=3 and i < 10:
        intervalo_3_9.append(i)

soma10_15 = sum(intervalo_10_15)
soma3_9 = sum(intervalo_3_9)

soma_tudo = soma10_15 / soma3_9
print("a razão dos intervalos pedidos é: ",soma_tudo)
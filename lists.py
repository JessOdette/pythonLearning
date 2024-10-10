import random

#Who will pay the bill?

participants = ["Alexis", "Jess", "Lucy", "Sergio", "Panky"]

payer = random.choice(participants)
print(payer + " will pay the bill today!")

#Suma la lista de numeros

numeros = [25, 50, 1, 2, 3, 4, 5, 10]

sum = 0
for i in range(len(numeros)):
    sum += numeros[i]

print(sum)

#Valor más grande

mayor = numeros[0]

for i in range(len(numeros)):
    if numeros[i] > mayor:
        mayor = numeros[i]

print(f"El número mayor es: {mayor}")

#Remove duplicated


'''
5. Faça um Programa que leia três números e mostre o maior e o menor deles
'''
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))
n3 = float(input("Informe o terceiro número: "))

if n1>n2 and n1>n3:
    maior = n1
elif n2>n1 and n2>n3:
    maior = n2
else:
    maior = n3

if n1<n2 and n1<n3:
    menor = n1
elif n2<n1 and n2<n3:
    menor = n2
else:
    menor = n3

  
print(f"O maior número foi: {maior: .2f}")
print(f"O menor número foi: {menor: .2f}")

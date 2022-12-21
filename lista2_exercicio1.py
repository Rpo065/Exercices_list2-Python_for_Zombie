'''
1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser 
um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno
'''
l1 = float(input("Informe o primeiro lado do triângulo: "))
l2 = float(input("Informe o segundo lado do triângulo: "))
l3 = float(input("Informe o terceiro lado do triângulo: "))

if l1 == l2 and l2 == l3:
    print("Triângulo equilátero")
elif l1 != l2 and l2 != l3 and l3 != l1:
    print("Triângulo escaleno")
else:
     print("Triângulo isósceles")

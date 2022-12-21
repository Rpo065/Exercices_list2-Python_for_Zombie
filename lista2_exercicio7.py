'''
7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a 
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem 
compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas
'''

area_pintada = float(input("Area a ser pintada mm²: "))
latas = area_pintada % 54

if latas != 0.0:
    lata_total = int(area_pintada/54)+1
else:
    lata_total = area_pintada/54

print(f'Quantidade de lata a ser comprada: {lata_total}')

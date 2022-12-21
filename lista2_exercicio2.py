'''
2. Determine se um ano é bissexto. Verifique no Google como fazer isso...

'''
import calendar
ano = int(input("Qual ano deseja saber se é bissexto: "))
ano_bissexto = calendar.isleap(ano)
if ano_bissexto:
    print("Ano bissexto")
else:
    print("Ano não bissexto")

calendar.isleap()
#Lista zmiennych liczb typu int i float:
Tabela_Liczb = [2, 4, 3, 2.5, 3.9, 1.9, 9, 5]
print(Tabela_Liczb)
for i in range(len(Tabela_Liczb)):
    Tabela_Liczb[i] = math.pow(Tabela_Liczb[i], 2)
print(Tabela_Liczb)


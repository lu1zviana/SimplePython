print('Programa de implementação de idade')

idade = int(input("Qual a sua idade? "))

if idade >= 5 and idade < 8:
    print('Você está na categoria infantil A')
elif idade >= 8 and idade < 11:
    print("Você está na categoria infantil B")
elif idade >= 11 and idade < 14:
    print('Você está na categoria Juvenil A')
elif idade >= 14 and idade < 17:
    print('Você está na categoria Juvenil B')
else:
    print('Você não se enquadra em nenhuma categoria específica')


print("")
print("")
print("")

idade2 = int(input("Qual sua idade? "));

if idade2 >= 16 and idade2 < 17:
	print("Menor");
elif idade2 >= 17 and idade2 < 18:
	print("Emancipado");
elif idade2 > 18:
	print("Maior");
else:
	print("Não se encaixa em nenhum!");
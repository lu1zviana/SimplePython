numero = int(input("Digite um numero: "));

if numero > 0:
	print(f"O {numero} eh positivo");
elif numero == 0:
	print(f"O {numero} eh igual a 0");
elif numero < 0:
	print(f"o {numero} eh negativo");
else:
	print("Não é um numero");
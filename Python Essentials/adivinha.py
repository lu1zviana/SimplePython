palpite = 0;
numero = 9;

while True: # Nós executamos sem verificar
	print("");
	print("QUAL O NUMERO CORRETO: ");
	palpite = int(input());
	if palpite == numero: # Estamos verificando nosso código
		print("Parabéns você acertou!");
		break
	else:
		print("Você errou!");
else:
	print("erro na aplicação!");
	print(bool(palpite));

"""def reduzirNumero(inteiro):
	while inteiro > 0:
		print(inteiro);
		inteiro = inteiro -1;

reduzirNumero(999999999999);

"""

"""
	1 - Checar se o nosso numero não é igual a 0;
	2 - se ele não for igual a 0 - iremos reduzir 1 unidade

	5 - 1;
	 4 - 1;
	  3 - 1;
	   2 - 1;
	    1 - 1;
	    -
	    0
///////////////////////////////////////////////////////////////////////////////////////


numeroInt = 10;

def reduzirNumero(numeroInt):
    if numeroInt > 0:
        # Remover 1 unidade / N - 1
        reduzirNumero(numeroInt = numeroInt - 1)

reduzirNumero(15)




def reduzirNumero(numeroInt):
    if numeroInt >= 0:
        print(numeroInt)
        reduzirNumero(numeroInt - 1)


reduzirNumero(5)

"""

# Fatorial sem recursão

def fatorialS(numero):
	fatorial = 1;
	if numero == 0:
		return 1
	else:
		for x in range(1, numero + 1):
			fatorial *= x;
		return fatorial



print(fatorialS(10));

# Fatorial - Solução Recursiva;
def fatorialR(numero):
	if numero == 0: $ Critério de parada;
		 return 1;
	else:
		# Parâmetro da chamada;
		return numero * fatorialR(numero - 1);



print(fatorialR(0));
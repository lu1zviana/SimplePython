#Paradigma imperativo

#bloco externo

"""

nome = "Gabriel" #variável global;

def minha_funcao():
	#bloco interno - o bloco interno de uma função é conhecido como corpo da função
	nome = "Ana"; #variavel local
	print(nome)


print(nome)
minha_funcao()



lista = [1,2,3,4,5,6]
print(lista)

retorno = lista.pop();
var1 = print("ola mundo");
print(lista)
print("Retorno da função pop:",retorno)
print("retorno da função print: ",var1)


def ola_mundo():
	return "ola mundo"

print(ola_mundo());


def par_impar():
	print("ola mundo")



par_impar();
"""

def olamundo():
	olamundo();
	print("ola mundo");

olamundo();
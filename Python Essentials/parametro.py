# PARÂMETROS DE UMA FUNÇÃO
"""


def minha_funcao():
	var = "Maria";
	return var;


print(minha_funcao());
var = "ana";
print(var)



def nome_da_funcao(parametro): # parâmetro é o nome dado aos valores na definição de uma função
	#corpo da função
	print(f"Olá {parametro}, seja bem vindo a nossa plataforma!");

nome = input("Qual é o seu nome? ");
nome_da_funcao(nome); # argumento é o nome dado aos valores utilizados na chamada de uma função


def imprime_nome(nome):
	print("Olá,", nome)

nome = input("Qual é o seu nome? ");

imprime_nome(nome);


def imprimir_nome(nome, sobrenome, idade):
	print(f"nome: {nome} \nsobrenome: {sobrenome} \nidade: {idade}");


imprimir_nome(sobrenome="luiz", idade="15", nome="felipe");



///////////////////////////////////////////////////////////////////////////////////////








#Parâmetro padrão - DEFINE ARGUMENTOS NÃO OBRIGATÓRIOS;

def imprimir_imovel(nomeImovel,n_quarto,vagasGaragem=None):
	print("Título: ", nomeImovel);
	print("Quartos: ", n_quarto);
	if vagasGaragem != None:
		print("Vagas na garagem", vagasGaragem);

#print()
#imprimir_nome();
print(30*"--")

#Exemplos de numero de argumentos <= n dos parametros
imprimir_imovel("Casa 3 Quartos - SP", 3);
print(30*"--")
imprimir_imovel("Apartamento - MG", 2, 1);

# Eemplos de numero de argumentos > numero dos parâmetros
imprimir_imovel("Loja comercial", 2, 0, "Desconto");




#Argumento Arbitário *Args - Essa função recebe argumentos que serão atruíbuidos em uma tupla

def imprimir_imovel(nomeImovel, n_quartos, VagasGaragem=None, *telefones):
	print(30*"--");
	print("Título:", nomeImovel);
	print("Quartos: ", n_quartos);
	if VagasGaragem != None:
		print("Vagas na Garagem: ", VagasGaragem);
	print("telefones", *telefones)


imprimir_imovel("Loja Comercial", 2 , 5, "55 11 99999-9999", "11 64 00383-4576");


################################################################################################







print(30*"--");

def imprimir_nomes(nomes):
	print(nomes[0]);



lista = ["ana", "beatriz", "pedro", "joão"];
imprimir_nomes(lista);


# Argumento Arbitário **Kwargs - Keyword Argument;
# Essa função recebe argumentos que serão atribuídos em um dicionário;



def imprimir_nomes(**nomes):
	print(f"{nomes['nomes']} {nomes['sobrenome']}");


imprimir_nomes(nomes="ana",sobrenome="julia");

"""

# ANOTHER VERSION DO CÓDIGO DE CIMA;

def imprimir_nomes(nomes):
	print(f"{nomes['nome']} {nomes['sobrenome']}");

dicio = {'nome': 'ana', 'sobrenome': 'kulia'}
imprimir_nomes(dicio);
"""

LISTA: Coleção ordenada, mutável e que permite valores duplicados;
TUPLAS: Coleção ordenada, imutável e que permite valores duplicados;
DICIONÁRIOS: Coleção não ordenada, mutável e que não permite valores duplicados;
"""

# Nós não precisar colocar chave pq quanto as listas e a tupla, elas tem index;

"""

lista = ["item1", "item2"];
tupla = ("item1", "item2") 

# chave:valor
dicio = {"chave1": "Gabriel", "chave2":"Luiz", "chave3":"Ana"};

print(dicio);

dicionario = {
	"nome":"Bruna",
	"idade":"27",
	"Nacionalidade":"Brasileira",
}

print(dicionario["idade"])

print(dicionario.get("idade"));

print(dicionario.keys());

if "idade" in dicionario:
	print("Achave idade existe");
	print(dicionario.items());



lista = ["item1","item2","item3"];
tupla = ("item1","item2","item3");

#chave:valor
dicio = {"nome":"Luiz","ano":"2008", "valor_logico":True}
print(dicio)

dicio["idade"] = 32

print(dicio);

dicio.update({"nome":"Ana"}) #Para trocar/adicionar um novo valor;
print(dicio);

"""

#dados = {"nome":"Luiz","ano":"2008", "valor_logico":True}
#print(dados)

dicio = {
	"dicio2": {
		"nome":"Luiz",
		"idade":"15",
	},
	"dicio3": {
		"nome":"Pedro",
		"idade":"25",
	}
}

print(dicio)

# A FUNÇÃO DO POPITEM ELIMINA O ULTIMO ITEM APENAS DA VERSÃO 3.7 E ACIMA
#dados.popitem() #nas outras versões (abaixo da 3.7) essa função elimina um item aleatório
#print(dados)

"""

dados.pop("nome"); #remover um item específico
print(dados)

del dados["ano"]; # deletar um item específico
print(dados)

dados.clear(); #remover tudo
print(dados)
"""


#for x in dados:
	#print(x);

#index      0       1       2
tupla = ("item1","item2","item3");
x = 0
dicio = dict.fromkeys(tupla,x);

print(dicio);


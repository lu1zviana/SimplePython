"""

lista = ["chicago", "queens", "salvador", "Pernambuco"];

print(lista);

lista2 = [2,3,7,8,10];
print(lista2);

lista3 = [2.0, 3.5, 6.3];
print(lista3);

lista2 = lista2 + lista3;
print(lista2);

lista4 = [True, False];
print(lista4);

lista5 = [True, "chicago", 2.5, False, 4, 8, 9];
print(lista5);

print(type(lista5));





####################### SLICING #######################



print(30 * "--")
print("SLICING\n")

print(lista5[::])

print(lista5[1:]); # Retorna do index que destacamos até o fim da lista;

print(lista5[2:]); #Retorna do index que destacamos até o fim da lista;

print(lista5[:3]); #Retorna do começo da lista até o index -1;

print(lista5[:4]); #Retorna do começo da lista até o index -1;

print(lista5[1:4]); #Retorna do index destacado até o index -1;

print(lista5[1:6:2]); #Está acrescentando em 2 em 2;

nome5 = "terra";

print(nome5[2:4]);
"""





###########################################################################






"""

lista1 = [2.0,3.5,4.7];
print(lista1);

lista2 = [1, 5, 9, 11, 15];
print(lista2);

# index     0        1        2          3          4         5
lista3 = ["gato","Cachorro", "Peixe", "Cavalo", "Tubarão", "Girafa"];

lista3[1] = "Cavalo";
print(lista3);

lista3[1:4] = ["Aguia", "Morcego", "Elefante"];
print(lista3);

lista3[1:2] = ['Águia', 'elefante'];
print(lista3)

lista3[1:6] = ["tubarão"];
print(lista3)

"""


"""
#Tamanho da lista - função len
print(len(lista1));
print(len(lista2));
print(len(lista3));

#Funcoes que só podem ser utlizadas com tipos de datos numéricos

print(30 * "--");
print(f"Somatórioa da lista1 {lista1} e da lista2 {lista2}");


print(sum(lista1)); #SOMATÓRIO DOS ELEMENTOS DA NOSSA LISTA
print(sum(lista2)); #SOMATÓRIO DOS ELEMENTOS DA NOSSA LISTA

print(30 * "--");
print(f"Valor máximo da lista1 {lista1} e da lista2 {lista2}");

print(max(lista2)); #Maior elemento da Lista;
print(max(lista1)); #Maior elemento da Lista;

print(30 * "--");
print(f"Valor mínimo da lista1 {lista1} e da lista2 {lista2}");

print(min(lista1)); #Menor elemento da Lista;
print(min(lista2)); #Menor elemento da Lista;

"""






###########################################################################




"""

nome = "Curso de Python";
valor = range(10);

print(nome);
print(valor);

lista7 = list(range(10));
print(lista7);

lista8 = list("Curso de Python");
print(lista8)

elemento = 8;

if elemento in lista7:
	print("Este elemento está dentro da lista");

"""











# index     0       1       2
#lista = ["Carro","Barco","Avião"];
#print(lista);

#lista.pop(0);
#lista.remove("Barco");

#del lista[0]




"""
carrinho_de_compras = ["pão","carne","verduras","Alface"];
carrinho_de_compras.sort(); #Ordenação/Algoritmo
"""





"""
lista = [1, 50, 23, 67, 100];
print(lista);

lista.sort(reverse = True);
print(lista);
"""


"""
lista = ["Ana","Pedro","Marta","Clarice","Beatriz"];

print(lista);

lista.sort(key = str.lower);
print(lista);

"""

#carrinho_de_compras.clear()

#print(carrinho_de_compras);


#for x in range(len(carrinho_de_compras)):
#	print(x, carrinho_de_compras[x]);







#lista.insert(1,["Bicicleta","Navio"])
#print(lista);

#lista.append(["Bicicleta","Navio"]);
#lista.extend(["bicicleta","navio"]);

#print(lista);
#print(len(lista));




"""
texto = "meunome@gmail.com";
lista2 = list(texto);
print(lista2);

texto = texto.split('@');
print(texto);

"""















"""
print(len(lista));

for x in range(3):
	print(x);

"""



lista = ['a','b','c'];
print(lista);

lista2 = lista.copy;
print(lista2);

lista2.append("d");

print(lista);
print(lista2)

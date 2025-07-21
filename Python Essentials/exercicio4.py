x = float(input("Qual o valor de x? "));
y = float(input("Qual o valor de y? "));

def resultado():
    if x > y:
        print("X é maior que Y")
    elif x < y:
        print("Y é maior que X")
    else:
        print("Os valores de x e y são iguais")

resultado();



print(30*"--");


base = int(input("Digite a base: "));
expoente = int(input("Digite o expoente: "));



def potenciacao(base,expoente):
	resultado = base ** expoente;
	return resultado;


resultado = potenciacao(base,expoente);
print(f"O resultado da potenciação é {resultado}");



print(30*"--");


valor = input("Que tipo de OPERADORES ARITMÉTICOS você quer usar? ")

conta1 = int(input("Qual o primeiro valor? "));
conta2 = int(input("Qual o segundo valor? "));

if valor == "+":
	results = conta1 + conta2;
elif valor == "-":
	results = conta1 - conta2;
elif valor == "*":
	results = conta1 * conta2;
elif valor == "**":
	results = conta1 ** conta2;
elif valor == "/":
	results = conta1 / conta2;
elif valor == "%":
	results = conta1 % conta2;

print(results);
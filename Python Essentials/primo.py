__doc__ = "Esse módulo tem como objetivo retornar se"
 "um numero é primo ou não";

#print(30 * "--")

def primo(numero):
    """
    Essa função tem como objetivo:
        retornar se um numero é primo ou não


    Parâmetros:
        1 parâmetro obrigatório - do tipo numérico inteiro
    """
    if numero > 1:
        for x in range(2, numero):
            if (numero % x) == 0:
                return "não é um Primo"
        else:
            return f"o {numero} é primo"
    else:
        return "Esse número não é primo: número menor ou igual a 1"

#print(30 * "--")

if __name == '__main':
    print(primo(5));
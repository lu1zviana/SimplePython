#import random
#from random import choice

"""from random import (
	random,
	choice
)"""

#from random import *

#lista = ["pedra","papel","tesoura"];

#print(randint(1,5))

"""
Módulos - arquivos com extensão .py - ou seja- arquivo python;
Pacotes - diretórios contendo um conjunto de módulos - pastas com vários arquivo python;
"""

from pacote import principal, segundario

print(principal.soma(2, 3));
print(segundario.quadratica(5));
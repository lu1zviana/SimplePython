import os

#Verificar se um arquivo existe
print(os.path.exists('texto.py'));
print(os.path.exists('teste.txt'));

#verififcar se um diretório existe
print(os.path.exists('python'));
print(os.path.exists('pastanova'));

# Exemplo de caminhos

print(os.path.exists('pastanova/texto.py'));

# Criando arquivos
#os.mknod('olamundo.py');



# Criando um diretório
#os.mkdir("python");



#caminho relativo
#os.mknod('./python/compas.txt');



#forma errada de usar caminho relativo
#os.mknod('arquivos/python/compras2.txt');

#os.mkdir('/home/louis/Documentos/python/ManipulacaoArquivos/loja')

#os.remove('teste.txt');

#os.remove('./pastanova/texto.py');

#os.rmdir('pastanova')

#os.rename('olamundo.txt','helloworld.txt')


#os.mknod('./python/compsas.txt')
#os.rename('./python/compsas.txt','./python/compras.txt');



print(30*'--')

"""
arquivo = open('./receitas/brigadeiro.txt');
print(arquivo.readline())
print(arquivo.closed)
arquivo.close();
print(arquivo.closed);

"""

with open('./receitas/brigadeiro.txt','a') as a:
	a.write(' padaria');

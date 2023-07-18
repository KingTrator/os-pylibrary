import os
# from time import sleep
# OBS: Pode ser preciso criar algumas pastas (criadas na aula1) para rodar este código.

# 0. "os.startfile()" abre arquivos com base no diretório e nome deles.
# IMPORTANTE: O with open() é uma opção melhor para abrir arquivos.
# 1. "os.rename()" renomeia arquivos.
# 2. "os.remove()" remove um arquivo. Combinado com os.rmdir(), permite eliminar lixo do sistema operacional.
# 3. "os.walk" é mais poderoso que o "os.listdir()", pois ele lista tanto arquivos quanto diretórios

#'''os.startfile(r'C:\Users\Win10\OneDrive\Desktop\TESTE2\oi.txt')'''

#'''sleep(2)'''  # Apenas para dar tempo ao código.
# Aliás, o fato de eu estar usando um "sleep(2)" reforça que a função with open() é mais eficiente que
# os.startfile, pois com with open() o arquivo seria fechado após ser executado, o que não geraria erro
# com a sequência de código abaixo, que renomeia o arquivo - o erro é porque o arquivo, provavelmente,
# ainda estava aberto quando a renomeação ocorreu.
# Embora, claro, o with open() não abra visualmente o arquivo e o uso de cada uma das funções é para fins distintos.
# Aqui está uma das razões para usar "os.chdir()", usar o método ".rename":
os.chdir(r'C:\Users\Win10\OneDrive\Desktop\TESTE2') # diretório no qual o loop de os.walk será aplicado.
#os.rename('oi.txt', 'ola.txt')'''

# para root, retorna-se a raiz do diretório (o nome do diretório que contém todos os demais.
# para dirs, retorna-se os diretórios dentro do diretório (as subpastas)
# para files, retorna-se os arquivos não diretórios (como 'exe') dentro da raiz pesquisada.

for root, dirs, files in os.walk(os.getcwd()):
    print(root)
    print(dirs)
    print(files)

# Este código é capaz de, a partir do cwd atual, ler todas
# as pastas e arquivos que estão presentes nela.
# Ou melhor, é possível montar um código que faça isso a partir deste loop,
# mas por hora eu apenas estou usando-o para dar um print em quais são as informações
# internas.
# "ROOT" inicia com o diretório principal, listando, então, files e dirs dentro dele.
# Depois, um dos diretórios secundários torna-se o novo "ROOT", no qual ocorrerá a listagem
# de diretórios internos e arquivos.
# Se não houver nada dentro, retorna-se uma lista vazia.

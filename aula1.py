import os


# INTRODUÇÃO:
# Usamos a biblioteca os para navegar nos diretórios existentes no
# computador. O módulo "os" tem várias das funções que eu já usava dentro do Prompt de Comando.
# 0. os.envrion = retorna um dicionário com as variáveis de ambiente.
# 0.1 Por meio de os.environ você pode usar ativamente as variáveis de ambiente, como fiz
# no projeto bot no repositório da selenium-library, usando a chave ['PATH'] para controlar esta variável de ambiente.
# 1. "os.getcwd()" diz o caminho da pasta atual.
# 2. "os.chdir(novo_caminho)" permite dar um novo cmainho, diferente do encontrado em getcwd inicialmente.
# 3. "os.mkdir()" cria um DIRETÓRIO dentro do diretório atual.
# 4. "os.listdir()" lista todos os diretórios dentro do diretório atual.
# IMPORTANTE: "os.listdir()" analise apenas diretórios, ou seja, não irá capturar um arquivo "exe", por exemplo.
# 5. "osmakedirs()" permite criar vários diretórios
# 6. "os.rmdir()" permite remover pastas VAZIAS (não pode conter nem subpastas nem arquivos).
sistema = os.environ
print(sistema)  # Retorna um dicionário
print(sistema['USERNAME'])  # Pega o valor da chave
print(os.getcwd())  # retorna a pasta atual
novo_caminho = r'C:\Users\Win10\OneDrive\Desktop'
os.chdir(novo_caminho)
print(os.getcwd())  # caminho mudou
os.mkdir('TESTE2')
print(os.listdir())

# Posso criar várias pastas sequencialmente com "os.makedirs()"
for i in range(5):
    if i <= 3:
        os.makedirs(rf'C:\Users\Win10\OneDrive\Desktop\Teste3\202{i}')

os.rmdir(r'C:\Users\Win10\OneDrive\Desktop\TESTE2')
# A pasta foi criada no exercício anterior, se não existir, retornará erro.
# A pasta do loop for não pode ser removida por esse método porque possui subpastas.

novo_caminho = r'C:\Users\Win10\OneDrive\Documentos\Estudos\python-libraries\os-pylibrary\os-pylibrary'
os.chdir(novo_caminho)  # voltei ao original

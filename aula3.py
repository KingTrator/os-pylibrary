import os

# 1. "os.path.basename()" permite pegar o nome da pasta atual
# 1.1. Diferente de os.getcwd() pois egar apenas o nome da pasta e não o caminho inteiro.
# No entanto, é preciso especificar o local de procura.
# Basicamente, ele retorna apenas a última informação que os.getcwd() daria
# 2. "os.path.commonpath()" permite pegar o caminho comum de diretórios seriados.
# 2.1. É particularmente útil em combinação com os.walk()
# 3. "os.path.commonprefix()" permite pegar a parte em comum de um caminho.
# Nota: "os.path.commonprefix()" é bem lixo, dei exemplo de uso por questão de honra, mas é bem lixo mesmo.
# 4. "os.path.dirname()", dado o CAMINHO COMPLETO de um arquivo, retorna o caminho no qual ele está inserido:
# IMPORTANTE (acho): "os.path.dirname()", à primeira vista, é meio inútil, contudo:
# 4.1 É útil para portabilidade. Ele trata de corrigir os caminhos para o sistema operacional em questão, exemplo:
# No Windows o separador de caminho é \, mas no Unix é /.
# 4.2 Se você tiver descoberto uma série de caminhos completos para vários arquivos por meio de os.walk, usar
# os.path.dirname() pode ser útil para fazer alguma leitura secundária.
# 5. "os.path.join()" usado para juntar strings em um único caminho.
# "os.path.join()" é um dos métodos mais poderosos que vi até agora.
print(os.getcwd())
caminho = r'C:\Users\Win10\OneDrive\Documentos\Estudos\python-libraries\os-pylibrary\os-pylibrary'
print(os.path.basename(caminho))
os.chdir(r'C:\Users\Win10\OneDrive\Desktop\Teste2')
# Abaixo eu crio um exemplo forçado que combina os.walk e os.path.commonpath()
c = 0
lista_caminhos = []
for root, _, _ in os.walk(os.getcwd()):
    if c == 0:
        pass
    else:
        lista_caminhos.append(root)
    c += 1
# Extraída a lista com os caminhos que se deseja analisar, pode-se
# botar pra quebrar com o os.path.commonpath()
# lista_caminhos = [] se a pasta estiver vazia, teremos uma exceção.
try:
    print(os.path.commonpath(lista_caminhos))
    print(os.path.commonprefix(lista_caminhos))  # Bem lixo mesmo
    print(os.path.dirname(lista_caminhos[0]))
except:
    print('Não há caminho em comum ou a pasta foi esvaziada.')
finally:
    print('-='*7, '... A SEGUIR ... JOIN', '-='*7)

# É BOM LEMBRAR: A exceção, nos blocos try/except é lançada
# somente quando se encontra uma linha de código que não funciona, mas
# as linhas anteriores serão executadas, se possíveis.
# Por isso, é bom pô-las em uma ordem de precedência, de modo a não corromper
# todo o código em caso de erro.
# Exemplo: se lista_caminhos[a] a =5, dá erro. Se isso estiver no começo, o restante, para o qual não dá erro,
# nem é executado. Se for ao final, a exceção é lançada só para essa linha.
# Pesando mais sobre isso, vi outra utilidade ao finally:
# digamos que uma parte do código não executa, no entanto, eu sei que sua não execução não compromete o restante do
# código. Se uma exceção for lançada, é possível que o resto do código não prossiga. Com finally, posso garantir que o
# restante do código será executado.
# Conversando com o ChatGPT-4, ele me disse que um bom uso do finally é, por exemplo, para aliviar o estresse de um
# servidor após uma série de operações ou para fechar um arquivo, que é algo que você provavelmente irá querer,
# ainda que o código não cumpra seu papel adequadamente.
drive = "C:"  # por alguma razão, não consigo por C:\ sem dar erro
usuario = 'Win10'
pasta = 'Teste2'
caminho = os.path.join(drive, r'\Users', usuario, 'Onedrive', 'Desktop', pasta)
print(caminho)
os.chdir(caminho)
print(os.listdir(os.getcwd()))

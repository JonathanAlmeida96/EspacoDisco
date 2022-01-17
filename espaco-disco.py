arquivo = 'usuarios.txt'


def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
    except:
        return False
    else:
        return True


def criarArquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Erro ao criar arquivo')
    else:
        print('Arquivo criado com sucesso!')


def lerArquivos(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('não foi possivel ler os arquivos!')
    else:
        return a


def transformarBytes(arq):
    a = lerArquivos(arq)
    transformado = []
    dic = {}
    for linha in a:
        dic.clear()
        dados = linha.split()
        nomes = dados[0]
        dados = dados[1]
        bytes = int(dados)
        bytes = bytes / 1048576
        dic['nome'] = nomes
        dic['megas'] = bytes
        transformado.append(dic.copy())
    return transformado


def calcularPorcentagem(arq):
    a = transformarBytes(arq)
    soma = 0
    soma2 = 0
    for n, c in enumerate(a):
        soma = soma2 + a[n]['megas']
        soma2 = soma
    soma = soma / 100
    divisao = 0
    divisao2 = []
    for n, c in enumerate(a):
        divisao = a[n]['megas'] / soma
        divisao2.append(divisao)
    return divisao2


def espacoUtilizado(arq):
    a = transformarBytes(arquivo)
    soma = 0
    soma2 = 0
    for n, c in enumerate(a):
        soma = soma2 + a[n]['megas']
        soma2 = soma
    return soma


def espacoMedio(arq):
    a = espacoUtilizado(arq)
    media = a / 6
    return media


if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

transformarBytes(arquivo)
informacoes = transformarBytes(arquivo)
porcentagem = calcularPorcentagem(arquivo)
total = espacoUtilizado(arquivo)
media2 = espacoMedio(arquivo)

print()
print(f'{"ACME Inc.":<18}Uso do espaço em disco pelos usuários')
print('-'*56)
print('-'*12)
print(f'Nr. usuário {"Espaço utilizado":>23}{"% do uso":>12}')
print()
for n, c in enumerate(informacoes):
    print(f'{n + 1}   ', end='')
    print(f'{c["nome"]:<15}{c["megas"]:>7.2f} MB {porcentagem[n]:>15.2f}%')
print()
print(f'Espaço total ocupado: {total:.2f} MB')
print(f'Espaço médio ocupado: {media2:.2f} MB')


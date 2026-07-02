from sistema.lib.interface import cabecalho

def arqexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerarq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        with open(arq, 'at') as a:
            a.write(f'{nome};{idade}\n')
            print(f'Novo registro de {nome} adicionado')
    except:
        print('Houve um erro na hora de escrever os dados')
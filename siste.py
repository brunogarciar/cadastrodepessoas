from sistema.lib.interface import *
from sistema.lib.arquivo import *
from time import sleep

arq = 'pessoas.txt'

if not arqexiste(arq):
    criararq(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar uma pessoa', 'Sair do programa'])
    if resposta == 1:
        lerarq(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Finalizando programa')
        break
    else:
        print('\033[35mErro opção inválida\033[m')
    sleep(1)


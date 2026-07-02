'''def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número válido! \033[m')
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar o número! \033[m')
            return 0
        else:
            return n'''
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mErro, Digite uma opção válida!\033[m')
        if ok:
            break
    return valor

def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c +=1
    print(linha())
    opc = leiaint('\033[33mSua opção:\033[m ')
    return opc




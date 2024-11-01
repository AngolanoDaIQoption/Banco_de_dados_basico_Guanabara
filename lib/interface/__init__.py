def leia_int(msg):
    while True:
        try:
            valor_int = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Voce inseriu valores invalidos!')
            continue
        except KeyboardInterrupt:
            print(f'\nO usuario preferiu nao inserir valor nenhum!')
            return None
        else:
            return valor_int


def linha(tam = 36):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(36))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for i,j in enumerate(lista):
        print(f'{i+1} - {j}')
    print(linha())
    opc = leia_int('Sua Opcao: ')
    if opc is None:
        return None
    return opc
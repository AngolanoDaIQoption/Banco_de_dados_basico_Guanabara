from BD_guanabara_.lib.interface import *
from BD_guanabara_.lib.arquivo import *
from time import sleep

arq = 'bancodedados.txt'

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Novo Cadastro', 'Sair do sistema'])

    if resp is None:
        cabecalho('Encerrando sistema pelo usuário...')
        break

    if resp == 1:
        print(f'Voce escolheu opcao {resp}')
        lerArquivo(arq)
        sleep(2)
        print(linha())
        escolha = input('Deseja deletar algum dado? (s/n): ').lower()
        numLinha = int(input('Insira o numero da linha: '))
        if escolha == 's':
            apagar_linha_por_numero(arq, numLinha-1)
            continue
        else:
            continue

    if resp == 2:
        print(f'Voce escolheu opcao {resp}')
        cabecalho('Novo Cadastro')

        nome = str(input('Nome: ')).strip()
        idade = leia_int('Idade: ')

        cadastrar(arq, nome, idade)

        continue

    if resp == 3:
        print(f'Voce escolheu opcao {resp}')
        cabecalho('Saindo do Sistema. Ate logo...')
        sleep(1)
        break

    else:
        print('So existem 3 opcoes...')
        sleep(0.6)
        continue



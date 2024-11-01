from BD_guanabara_.lib.interface import *

def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criacao do arquivo!!')
    else:
        print(f'Arquivo {nome} com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('Pessoas Cadastradas')
        for linha, j in enumerate(a):
            dado = j.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{linha+1} {dado[0]:<28}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome = 'Desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do banco de dados!!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de ADICIONAR os dados no banco de dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')


def apagar_linha_por_numero(nome_arquivo, numero_linha):
    with open(nome_arquivo, 'r') as file:
        linhas = file.readlines()

    if 0 <= numero_linha < len(linhas):
        del linhas[numero_linha]
        with open(nome_arquivo, 'w') as file:
            file.writelines(linhas)
        print(f"Linha {numero_linha + 1} excluída com sucesso.")
    else:
        print("Número de linha inválido.")



#aula9 - arquivos 30/07/2021
import shutil

# arquivo = open('teste.txt','w')
# arquivo.write('Minha primeira escrita')
# arquivo.close()

# arquivo = open('teste.txt', 'a')
# arquivo.write('\nTerceira linha')
# arquivo.close()

def escrever_arquivo(diretorio, texto):
    arquivo = open(diretorio, 'w')
    arquivo.write(texto+'\n')
    arquivo.close()

def atualizar_arquivo(diretorio, texto):
    arquivo = open(diretorio, 'a')
    arquivo.write(texto+'\n')
    arquivo.close()


def ler_arquivo(diretorio):
    arquivo = open(diretorio, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(diretorio):
    arquivo = open(diretorio, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas])/4
        print(f'Aluno: {aluno} e sua média é {media(lista_notas)}')

def copiar_arquivo(nome_arquivo,novo_caminho):
     shutil.copy(nome_arquivo,novo_caminho)


def mover_arquivo(nome_arquivo,novo_caminho):
    shutil.move(nome_arquivo,novo_caminho)

if __name__ == '__main__':

    selecao = int(input('1 ou 2'))
    nome_arquivo = input('Digite nome do arquivo:')

    if selecao == 1:
        texto = input('Digite o texto:')
        diretorio = 'e:/WORKSPACE/app.python/' + nome_arquivo
    else:
        novo_caminho = input('informe novo local:')+'/'


    opcao = int(input('1(novo), 2(atualizar), 3(ler), 4(Alunos) 5(copiar) 6(mover)'))
    if opcao == 1:
        escrever_arquivo(nome_arquivo,texto)
    elif opcao == 2:
        atualizar_arquivo(nome_arquivo,texto)
    elif opcao == 3:
        ler_arquivo(nome_arquivo)
    elif opcao == 4:
        media_notas(nome_arquivo)
    elif opcao == 5:
        copiar_arquivo(nome_arquivo,novo_caminho)
    elif opcao == 6:
        mover_arquivo(nome_arquivo,novo_caminho)
    else:
        print('selecione uma opção válida!')



import sqlite3
from time import sleep
import datetime

def linha():
    print('-=-' * 30)

cores = {'limpa': '\033[m',
         'linhaverde': '\033[4:32m',
         'negritoazul': '\033[1:34m',
         'negritoamarelo': '\033[1:33m',
         'negritoazulmarinho': '\033[1:36m'}

print('oi')

print('Bem vindo ao {}TOgabDO{}! O melhor programa via Console de controle de tarefas!'.format(cores['negritoamarelo'], cores['limpa']))
sleep(0.5)
print('~~~~ Configurando ambiente ~~~')
sleep(1)

conexao = sqlite3.connect('MS24.sqlite3')
cursor = conexao.cursor()


nome = str(input('Digite seu nome completo: '))

print('Olá {}{}{}! Vamos iniciar?'.format(cores['negritoamarelo'], nome, cores['limpa']))
    
sleep(1)

while True:
    linha()
    print('                -=- MENU -=-')
    print('*Para criar novas categorias digite 1.\n*Para atualizar uma categoria existente digite 2.\n*Para excluir uma categoria existente digite 3.\n*Para listar todas as categorias digite 4.\n*Para criar uma nova atividade digite 5.\n*Para mostrar todos os compromissos de hoje digite 6.\n*Para alterar o status de uma tarefa, digite 7.\n*Para encerrar o programar digite 8.')
    linha()
    opcaoMenu = int(input(f'Usuário {nome}! O que você gostaria de fazer agora? '))
    linha()
    if opcaoMenu == 1:
        '''Para criar uma nova categoria'''
        nomeCategoria = str(input('Digite o nome da categoria que deseja inserir: ')).upper
        valoresCategoria = [nomeCategoria]
        insercaoNovaCategoria = 'INSERT INTO tbcategories (nomecategoria) values (?)'
        cursor.execute(insercaoNovaCategoria, valoresCategoria)
        conexao.commit()
        valoresCategoria.clear()
        print(f'Categoria {nomeCategoria} adiciona com sucesso!')

    if opcaoMenu == 2:
        '''Para atualizar alguma categoria'''
        categoriaAtual = str(input('Para atualizar o nome da categoria, insira primeiro o nome atual da categoria: ')).upper
        categoriaNova = str(input('E agora insira o NOVO nome dessa categoria: ')).upper
        alteracaoCategoria = 'UPDATE tbcategories set nomecategoria = ? where nomecategoria = ?'
        novosdadosCategoria = [categoriaNova, categoriaAtual]
        cursor.execute(alteracaoCategoria, novosdadosCategoria)
        conexao.commit()
        novosdadosCategoria.clear()
        print(f'Categoria atualizada com sucesso!')

    if opcaoMenu == 3:
        '''Para deletar alguma categoria'''
        categoriaExcluir = str(input('Digite o nome da categoria que deseja excluir: ')).upper
        decisaoExclusao = str(input('Você tem certeza que deseja excluir? S/N: ')).upper()
        if decisaoExclusao not in 'SN':
            decisaoExclusao = str(input('Opção inválida. Digite novamente S/N: ')).upper()
        if decisaoExclusao == 'N':
            print('Ok, não excluiremos.')
            
        if decisaoExclusao == 'S':
            exclusaoCategoria = 'DELETE FROM tbcategories where nomecategoria = ?'
            valorExclusao = [categoriaExcluir]
            cursor.execute(exclusaoCategoria, valorExclusao)
            conexao.commit()
            valorExclusao.clear()
            print('Categoria Excluída com sucesso!')

    if opcaoMenu == 4:
        '''Para visualizar todas as categorias'''
        visualizardadosCategoria = 'SELECT * FROM tbcategories'
        consulta = cursor.execute(visualizardadosCategoria)
        print('|ID|', '| Nome da Categoria |' )
        for resultado in consulta:
            print(resultado)    
    
    if opcaoMenu == 5:
        '''Para visualizar todas as categorias'''
        visualizardadosCategoria = 'SELECT * FROM tbcategories'
        consulta = cursor.execute(visualizardadosCategoria)
        print('|ID|', '| Nome da Categoria |' )
        for resultado in consulta:
            print(resultado)
        linha()
        '''Para visualizar os status disponíveis'''
        visualizadorStatus = 'SELECT * FROM tbstatus'
        consulta = cursor.execute(visualizadorStatus)
        print('|ID|', '| Nome do Status |' )
        for i in consulta:
            print(i)
        '''Para criar uma nova atividade'''
        nomeAtividade = str(input('Digite o nome da atividade: ')).upper
        idCategoria = int(input('Baseado na lista dos Ids das categorias acima, digite o ID que será a categoria da sua atividade: '))
        nomeStatus = int(input('Baseado na lista dos Ids dos STATUS acima, digite o ID que está o status da sua atividade: '))
        data = input('Qual a data dessa tarefa? Por favor, digite no formato ano-mes-dia:  ')
        nomeResponsavel = str(input('Por favor digite o nome do responsável dessa tarefa: ')).upper
        insercaoNovaAtividade = 'INSERT INTO tbactivities (nomeatividade, categoriaid, statusid, data, responsavel) values (?, ?, ?, ?, ?)'
        listaAtividade = [nomeAtividade, idCategoria, nomeStatus, data, nomeResponsavel]
        cursor.execute(insercaoNovaAtividade, listaAtividade)
        conexao.commit()
        listaAtividade.clear

    if opcaoMenu == 6:
        '''Para mostrar todas as atividades de algum dia especifico'''
        dataEspecifica = input('Digite a data que você gostaria visualizar as atividades no formato ano-mes-dia: ')
        responsavelEspecifico = input('Digite o nome do responsável pelas tarefas: ').upper
        visualizadorTarefas = "SELECT p.nomeatividade, p.data, p.responsavel FROM tbactivities as p where data like ? and responsavel = ?"
        listaData = [dataEspecifica, responsavelEspecifico]
        consulta = cursor.execute(visualizadorTarefas, listaData)
        conexao.commit()
        print('Lista de tarefas com os filtros selecionados: ')
        for i in consulta:
            print(i)
        listaData.clear
    

    if opcaoMenu == 7:
        sleep(1)
        filtroTarefa = input('Qual tarefa gostaria de alterar o status: ')
        sleep(1)
        visualizadorStatus = 'SELECT * FROM tbstatus'
        consulta = cursor.execute(visualizadorStatus)
        print('|ID|', '| Nome do Status |' )
        for i in consulta:
            print(i)
        sleep(0.5)
        novoStatus = int(input('Digite o novo status da sua tarefa: '))
        atualizador = 'UPDATE tbactivities set statusid = ? where nomeatividade = ?'
        atualizacaodeDados = [novoStatus, filtroTarefa]
        cursor.execute(atualizador, atualizacaodeDados)
        conexao.commit()
        atualizacaodeDados.clear
        sleep(0.5)
        print('Status atualizado!')
    
    if opcaoMenu == 8:
        print(f'Volte sempre {nome}!')
        break

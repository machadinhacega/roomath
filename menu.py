# #MENU
from funcoes import adicionarUsuario
from funcoes import editarUsuario
from funcoes import excluirUsuario
from funcoes import adicionarConta
from funcoes import consultarConta
from funcoes import statusConta
from funcoes import editarConta
from funcoes import excluirConta


todos = []
contas = {}

while True:
    escolha1 = input(
        '\n###############################\n########## ROOMATH ###########\n###############################'
        '\n____________________________\nEscolha sua opção\n1 - Gerenciar perfil de usuário \n2 - Gerenciar Contas '
        '\n3 - Mostrar Valor \n0 - Fechar o programa\n►  ')

    if escolha1 == '1':
        while True:
            escolha1 = input(
                '____________________________\n##### GERENCIAR PERFIL #####\nEscolha sua opção\n1 - Adiconar perfil '
                '\n2 - Editar perfil \n3 - Excluir perfil \n4 - Mostrar Perfis\n0 - Voltar para o menu anterior\n►  ')
            if escolha1 == '1':
                print('##### Adicionar #####')
                adicionarUsuario(todos)

            elif escolha1 == '2':
                print('##### Editar #####')
                editarUsuario(todos)

            elif escolha1 == '3':
                print('##### Excluir #####')
                excluirUsuario(todos)

            elif escolha1 == '4':
                for nomes in todos:
                    print (nomes)
                input('Digite ENTER para continuar')
            elif escolha1 == '0':
                break

            else:
                print('Digite uma opção válida')

    elif escolha1 == '2':
        print('##### GERENCIAR CONTAS #####')
        while True:
            opcao = input("""Escolha uma opção:
        1 - Adicionar conta
        2 - Consultar contas
        3 - Ver todas as contas
        4 - Buscar conta por status
        5 - Editar
        6 - Excluir
        7 - Voltar
        ►""")

            # ## Adicionar
            if opcao == '1':
                adicionarConta(contas)

            ## Consultar
            if opcao == '2':
                consultarConta(contas)

            # Ver todas as contas
            if opcao == '3':
                for k, v in contas.items():
                    print('\nDados da conta de {}: '.format(k))
                    for k, v in contas[k].items():
                        print(k, ': ', v)

            # Buscar conta por status
            if opcao == '4':
                statusConta(contas)

            # Editar
            if opcao == '5':
                editarConta(contas)

            # Excluir
            if opcao == '6':
                excluirConta(contas)

            # Voltar
            if opcao == '7':
                break

    elif escolha1 == '3':
        print('##### MOSTRAR VALORES #####')
        print('Fulano deve tanto pra Sicrano')
        input('Digite ENTER para continuar')
    elif escolha1 == '0':
        print('Volte sempre!')
        break
    else:
        print('Digite uma opção válida')









#ANOTAÇÕES SOBRE O MENU

###Gerenciar Perfil
## Adicionar
## Editar
## Excluir
## Voltar

###Gerenciar Contas
## Adicionar
## Consultar
# Ver todas as contas
# Buscar conta por nome
# Buscar conta por status
## Editar
## Excluir
## Voltar

###Mostrar Valor
#Dividir o valor

###Cancelar














#
# elif escolha1 == '2':
#     print('##### Editar #####')
#     #         edit = input ('Você deseja editar algum usuário? ')
#     #         while edit == 'sim':
#     #             print (todos)
#     #             edit2 = [print ('Escolha o usuário a ser editado: ')]
#
#
#
# elif escolha1 == '0':
#     break
#
# else:
#     print('Digite uma opção válida')
#
# elif escolha1 == '2':
#     print('##### GERENCIAR CONTAS #####')
# while True:
#     escolha1 = input(
#         '____________________________\n##### GERENCIAR CONTAS #####\nEscolha sua opção\n1 - Adiconar conta
#         \n2 - Editar conta \n3 - Excluir conta \n0 - Voltar para o menu anterior\n►  ')
#
#     if escolha1 == '1':
#         print('##### Adicionar #####')
#         nomeconta = input('Digite o nome da sua conta: ')
#         valorconta = input('Digite o valor da conta: ')
#     elif escolha1 == '2':
#         print('##### Editar conta #####')
#
#     elif escolha1 == '3':
#         print('##### Excluir conta #####')
#
#     elif escolha1 == '0':
#         break
#
#     else:
#         print('Digite uma opção válida')
#
# elif escolha1 == '3':
#     print('##### MOSTRAR VALORES #####')
#     print('Fulano deve tanto pra Sicrano')
#     input('Digite ENTER para continuar')
# elif escolha1 == '0':
#     print ('Volte sempre!')
#     break
# else:
#     print ('Digite uma opção válida')
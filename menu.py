# #MENU
todos = []
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
                nomeusuario = input('Digite seu nome: ').title()
                todos.append(nomeusuario)
                print('Seja bem vindo ao Roomath,', nomeusuario)
                while True:
                    questNovoUsuario = input('Você gostaria de adicionar mais um perfil? ').lower()
                    if questNovoUsuario == 'sim':
                        nomeusuario = input('Digite um novo nome: ')
                        todos.append(nomeusuario)
                        print('Seja bem vindo ao Roomath,', nomeusuario)
                    elif questNovoUsuario == 'não':
                        break
                    else:
                        print('Por favor, digite SIM ou NÃO.')

            elif escolha1 == '2':
                print('##### Editar #####')

            elif escolha1 == '3':
                print('##### Excluir #####')
                print('Lista de perfis:\n', todos)
                excluirUsuario = input('Digite o nome do usuário a ser excluído: ').title()
                todos.remove(excluirUsuario)
                print('Lista de perfis atualizada:\n', todos)
                while True:
                    questExcluirUsuario = input('Você deseja excluir outro usuário? ').lower()
                    if questExcluirUsuario == 'sim':
                        excluirUsuario = input('Digite o nome do usuário a ser excluído: ').title()
                        todos.remove(excluirUsuario)
                        print('Lista de perfis atualizada:\n', todos)
                    elif questExcluirUsuario == 'não':
                        break
                    else:
                        print('Por favor, digite SIM ou NÃO.')

            elif escolha1 == '4':
                print('Lista de perfis:\n', todos)
                input('Digite ENTER para continuar')
            elif escolha1 == '0':
                break

            else:
                print('Digite uma opção válida')

    elif escolha1 == '2':
        print('##### GERENCIAR CONTAS #####')
        while True:
            escolha1 = input(
                '____________________________\n##### GERENCIAR CONTAS #####\nEscolha sua opção\n1 - Adiconar conta '
                '\n2 - Editar conta \n3 - Excluir conta \n0 - Voltar para o menu anterior\n►  ')

            if escolha1 == '1':
                print('##### Adicionar #####')
                nomeconta = input('Digite o nome da sua conta: ')
                valorconta = input('Digite o valor da conta: ')
            elif escolha1 == '2':
                print('##### Editar conta #####')

            elif escolha1 == '3':
                print('##### Excluir conta #####')

            elif escolha1 == '0':
                break

            else:
                print('Digite uma opção válida')

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
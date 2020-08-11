# #MENU
while True:
    escolha1 = input(
        '\n###############################\n########## ROOMATH ###########\n###############################\n____________________________\nEscolha sua opção\n1 - Gerenciar perfil de usuário \n2 - Gerenciar Contas \n3 - Mostrar Valor \n0 - Fechar o programa\n►  ')

    if escolha1 == '1':
        while True:
            escolha1 = input(
                '____________________________\n##### GERENCIAR PERFIL #####\nEscolha sua opção\n1 - Adiconar perfil \n2 - Editar perfil \n3 - Excluir perfil \n0 - Voltar para o menu anterior\n►  ')

            if escolha1 == '1':
                print('##### Adicionar #####')
                nomeusuario = input('Digite seu nome: ')
            elif escolha1 == '2':
                print('##### Editar #####')

            elif escolha1 == '3':
                print('##### Excluir #####')

            elif escolha1 == '0':
                break

            else:
                print('Digite uma opção válida')

    elif escolha1 == '2':
        print('##### GERENCIAR CONTAS #####')
        while True:
            escolha1 = input(
                '____________________________\n##### GERENCIAR CONTAS #####\nEscolha sua opção\n1 - Adiconar conta \n2 - Editar conta \n3 - Excluir conta \n0 - Voltar para o menu anterior\n►  ')

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


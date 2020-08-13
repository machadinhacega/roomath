if escolha1 == '1':
    print('##### Adicionar #####')
    todos = []
    nomeusuario = input('Digite seu nome: ')
    todos.append(nomeusuario)
    print('Seja bem vindo ao Roomath,', nomeusuario)
    novousuario = input('Você gostaria de adicionar mais um perfil? ')
    while novousuario == 'sim':
        print('##### Adicionar #####')
        nomeusuario = input('Digite seu nome: ')
        todos.append(nomeusuario)
        print('Seja bem vindo ao Roomath,', nomeusuario)
        novousuario = input('Você gostaria de adicionar mais um perfil? ')
        # print (todos)
    if novousuario == 'não':
        print('Retorne ao menu inicial')
        # print (todos)

elif escolha1 == '2':
    print('##### Editar #####')
    #         edit = input ('Você deseja editar algum usuário? ')
    #         while edit == 'sim':
    #             print (todos)
    #             edit2 = [print ('Escolha o usuário a ser editado: ')]

elif escolha1 == '3':
    print('##### Excluir #####')
    excluir1 = input('Você deseja ver a lista de usuários? ')
    while excluir1 == 'sim':
        print(todos)
        perg1 = input('Você deseja excluir algum usuário? ')
        if perg1 == 'sim':
            perg2 = input('Digite o nome do usuário a ser excluído: ')
            # O programa tá quebrando quando digito algum nome que está na lista de forma "errada" como resolver?
            todos.remove(perg2)
    while excluir1 == 'não':
        # o programa não está entrando no laço de repetição do "não" entender pq
        print('Volte para o menu inicial')
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
    print ('Volte sempre!')
    break
else:
    print ('Digite uma opção válida')
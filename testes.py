todos = []
contas = {}
while True:
    escolha1 = input("""###############################
########## ROOMATH ###########
###############################
____________________________
Escolha sua opção
1 - Gerenciar perfil de usuário 
2 - Gerenciar Contas 
3 - Mostrar Valor 
0 - Fechar o programa
►  """)

#Gerenciar perfil de usuário
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
        from funcoes_contas import adicionarConta
        from funcoes_contas import consultarConta
        from funcoes_contas import buscarContaStatus
        from funcoes_contas import editarConta
        from funcoes_contas import excluirConta
        print('##### GERENCIAR CONTAS #####')
        while True:
            opcao = input("""Escolha uma opção:
1 - Adicionar
2 - Consultar
3 - Ver todas as contas
4 - Buscar conta por status
5 - Editar
6 - Excluir
0 - Voltar
►  """)
            if opcao == '1':
                adicionarConta(contas)
            if opcao == '2':
                consultarConta(contas)
            if opcao == '3':
                if contas:
                    for k, v in contas.items():
                        print('\nDados da conta de {}: '.format(k))
                        for k, v in contas[k].items():
                            print(k, ': ', v)
                    input('Digite ENTER para continuar')
                else:
                    print('Você não tem nenhuma conta cadastrada')
                    input('Digite ENTER para continuar')
            if opcao == '4':
                buscarContaStatus(contas)
            if opcao == '5':
                editarConta(contas)
            if opcao == '6':
                excluirConta(contas)
            if opcao == '0':
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
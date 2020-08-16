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
                        nomeusuario = input('Digite um novo nome: ').title()
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

#Gerenciar Contas
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
                nomeConta = input('Digite o nome da conta que deseja adicionar: ').title()
                valor = input('Valor da conta de {}: '.format(nomeConta))
                while valor.isnumeric() == False:
                    valor = input('Digite um valor válido: ')
                status = input("Qual a situação da conta de {}? (Pago ou Em aberto): ".format(nomeConta)).title()
                while status != 'Pago' and status != 'Em Aberto':
                    status = input("Por favor, digite uma das opções a seguir (Pago ou Em aberto): ").title()
                contas[nomeConta] = {
                    'Valor': float(valor),
                    'Status': status,
                    'Pagante': 'Ninguém pagou ainda :('
                }
                if contas[nomeConta]['Status'] == 'Pago':
                    contas[nomeConta]['Pagante'] = input('Quem pagou a conta: ').title()

                print('Conta de {} adicionada.'.format(nomeConta))

            ## Consultar
            if opcao == '2':
                consultarConta = input('Digite a conta que deseja consultar: ').title()
                while consultarConta not in contas:
                    print(
                        'A conta "{}" não esta cadastrada. Escolha uma das contas cadastradas:'.format(consultarConta))
                    for k, v in contas.items():
                        print(k, end='. ')
                    consultarConta = input('\nDigite uma conta válida: ').title()
                print('Dados da conta de {}'.format(consultarConta))
                for k, v in contas[consultarConta].items():
                    print(k, ': ', v)

            # Ver todas as contas
            if opcao == '3':
                for k, v in contas.items():
                    print('\nDados da conta de {}: '.format(k))
                    for k, v in contas[k].items():
                        print(k, ': ', v)

            # Buscar conta por status
            if opcao == '4':
                statusBusca = input('Você deseja buscar contas "Pagas" ou "Em aberto"? ').lower()
                while statusBusca != 'pagas' and statusBusca != 'em aberto':
                    statusBusca = input('Por favor, digite uma das opções a seguir (Pagas ou Em aberto): ').lower()
                    for k, v in contas.items():
                        print(k, end='. ')
                if statusBusca == 'pagas':
                    print('\nContas Pagas: ')
                    for conta, v in contas.items():
                        for k, v in contas[conta].items():
                            if v == 'Pago':
                                print(conta, end='. ')
                elif statusBusca == 'em aberto':
                    print('\nContas Em Aberto: ')
                    for conta, v in contas.items():
                        for k, v in contas[conta].items():
                            if v == 'Em Aberto':
                                print(conta, end='. ')

            # Editar
            if opcao == '5':
                nomeConta = input('Digite o nome da conta que deseja Editar: ').title()
                while nomeConta not in contas:
                    print('A conta "{}" não esta cadastrada. Escolha uma das contas cadastradas:'.format(nomeConta))
                    for k, v in contas.items():
                        print(k, end='. ')
                    nomeConta = input('\nDigite uma conta válida: ').title()

                print('Dados anteriores da conta de {}'.format(nomeConta))
                for k, v in contas[nomeConta].items():
                    print(k, ': ', v, end=' | ')
                print('\n')

                valor = input('Novo valor da conta de {}: '.format(nomeConta))
                while valor.isnumeric() == False:
                    valor = input('Digite um valor válido: ')
                status = input("Nova situação da conta de {}? (Pago ou Em aberto): ".format(nomeConta)).title()
                while status != 'Pago' and status != 'Em Aberto':
                    status = input("Por favor, digite uma das opções a seguir (Pago ou Em aberto): ").title()
                contas[nomeConta] = {
                    'Valor': float(valor),
                    'Status': status,
                    'Pagante': 'Ninguém pagou ainda :('
                }
                if contas[nomeConta]['Status'] == 'Pago':
                    contas[nomeConta]['Pagante'] = input('Quem pagou a conta: ').title()
                print('\nConta de {} editada com sucesso.'.format(nomeConta))

            # Excluir
            if opcao == '6':
                nomeConta = input('Digite o nome da conta que deseja Editar: ').title()
                while nomeConta not in contas:
                    print('A conta "{}" não esta cadastrada. Escolha uma das contas cadastradas:'.format(nomeConta))
                    for k, v in contas.items():
                        print(k, end='. ')
                    nomeConta = input('\nDigite uma conta válida: ').title()
                contas.pop(nomeConta)
                print(contas)

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



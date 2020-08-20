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

    if escolha1 == '1':
    # Gerenciar perfil de usuário
        from funcoes import adicionarUsuario
        from funcoes import editarUsuario
        from funcoes import excluirUsuario
        while True:
            escolha1 = input("""##### GERENCIAR PERFIL #####
Escolha sua opção
1 - Adiconar perfil 
2 - Editar perfil 
3 - Excluir perfil 
4 - Mostrar Perfis
0 - Voltar para o menu anterior
►  """)
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
                if todos:
                    for nomes in todos:
                        print (nomes)
                else:
                    print('Você não tem usuários cadastrados')
                input('Digite ENTER para continuar')
            elif escolha1 == '0':
                break

            else:
                print('Digite uma opção válida')


    elif escolha1 == '2':
    # Gerenciar Contas
        from funcoes import adicionarConta
        from funcoes import consultarConta
        from funcoes import buscarContaStatus
        from funcoes import editarConta
        from funcoes import excluirConta

        print('##### GERENCIAR CONTAS #####')
        while True:
            opcao = input("""Escolha uma opção:
1 - Adicionar conta
2 - Consultar contas
3 - Ver todas as contas
4 - Buscar conta por status
5 - Editar
6 - Excluir
0 - Voltar
►  """)
            if opcao == '1':
                adicionarConta(contas,todos)
            elif opcao == '2':
                consultarConta(contas)
            elif opcao == '3':
                if contas:
                    for k, v in contas.items():
                        print('\nDados da conta de {}: '.format(k))
                        for k, v in contas[k].items():
                            print(k, ': ', v)
                    input('Digite ENTER para continuar')
                else:
                    print('Você não tem nenhuma conta cadastrada')
                    input('Digite ENTER para continuar')
            elif opcao == '4':
                buscarContaStatus(contas)
            elif opcao == '5':
                editarConta(contas)
            elif opcao == '6':
                excluirConta(contas)
            elif opcao == '0':
                break
            else:
                print('Digite uma opção válida')

    elif escolha1 == '3':
        print('##### MOSTRAR VALORES #####')
        input('Digite ENTER para continuar')


    elif escolha1 == '0':
        print('Volte sempre!')
        break

    else:
        print('Digite uma opção válida')


# ------------------------------------------------------------------------------------------------
# ---------------------------- ENVIANDO E-MAIL -----------------------------------------
# ------------------------------------------------------------------------------------------------
## Aqui é pra se a pessoa quiser enviar um lembrete pra pagar as contas e plau
# from funcoes_email import enviandoLembrete
# #enviandoLembrete()
#
## Enviando um e-mail de cobrança
# questEnviar = input('Quer enviar uma mesagem para pessoa que te deve?\n► ').lower()
# while questEnviar != 'sim' and questEnviar != 'não':
#     questEnviar = input('PQP, digita "sim" ou "não" carai. Anitta sabe...\n► ')
# if questEnviar == 'sim':
#     from funcoes_email import sendEmailCobranca
#     sendEmailCobranca(input('E-mail para envio: '),input('Valor pra Cobrar: '),input('Digite o código do boleto: '))
#     print('\nE-mail enviado com sucesso!')
# elif questEnviar == 'não':
#     print('Tudo bem, mas não esqueça de avisá-la')
#     input('Digite ENTER para continuar')
import csv
import os
from time import sleep
todos = []
contas = {}


saudacao = """Olá, seja bem vinde ao Roomath, a combinação perfeita no fim do mês.
pow pow pei pow. *Fogos de Alegria*
Você é nova por aqui ou já é cadastrade?
(Digite "nova" ou "cadastrade")"""
# for i in saudacao:
#     sleep(0.05)
#     print(i, end='')
print(saudacao)

# Verificando se a pessoa ja é cadatrada. Caso não seja, o programa vai criar uma planilha nova
questInicio = input('\n► ').lower()
while questInicio not in 'nova cadastrade cadastrado cadastrada':
    questInicio = input('Não entendi, você é nova ou cadastrade?\n► ')

if questInicio == 'nova':
    # Criando as planilhas se a pessoa for NOVA
    contas = {}
    todos = []
    with open('roomath_contas.csv', 'w', newline='') as csvfile:
        fieldnames = []
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    with open('roomath_perfis.csv', 'w', newline='') as csvfile:
        fieldnames = []
        writer2 = csv.DictWriter(csvfile, fieldnames=fieldnames)

elif questInicio == 'cadastrado' or questInicio == 'cadastrada' or questInicio == 'cadastrade':
    # Acessando planilha: Atualizando nosso código com os dados da planilha Existente
    contas = {}
    todos = []
    if os.path.exists('./roomath_contas.csv') and os.path.exists('./roomath_perfis.csv'):
        with open('roomath_contas.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contas[row['Conta']] = {'Valor': float(row['Valor']), 'Status': row['Status'], 'Pagante': row['Pagante']}

        with open('roomath_perfis.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                todos.append(row['Perfil'])
    else:
        print('CARALHO, TU MENTE NÉ?\nVocê não tem nenhum dado, mas as gente é legal e te cadastrou aqui.')
        with open('roomath_contas.csv', 'w', newline='') as csvfile:
            fieldnames = []
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        with open('roomath_perfis.csv', 'w', newline='') as csvfile:
            fieldnames = []
            writer2 = csv.DictWriter(csvfile, fieldnames=fieldnames)


while True:
    escolha1 = input("""\n###############################
########## ROOMATH ###########
###############################
____________________________
Escolha sua opção
1 - Gerenciar perfil de usuário 
2 - Gerenciar Contas 
3 - Mostrar Valor 
0 - Salvar os dados e Sair
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
                print('Opção ínválida')
                input('Digite ENTER para continuar ')


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
                editarConta(contas, todos)
            elif opcao == '6':
                excluirConta(contas)
            elif opcao == '0':
                break
            else:
                print('Opção ínválida')
                input('Digite ENTER para continuar ')

    elif escolha1 == '3':
        print('##### MOSTRAR VALORES #####')
        while True:
            # Verificando se "TODOS" NÃO ta vazio
            if todos:
                # Verificando se "CONTAS" NÃO ta vazio
                if contas:
                    opcaofinal = input("""
Escolha uma opção:
1 - Total de despesas
2 - O que foi pago por cada usuário
3 - Quem deve a quem e quanto
0 - Voltar
►  """)
                    # valor total das depesas da casa
                    valorTotal = 0
                    valorTotalPago = 0
                    for conta in contas:
                        valorTotal += contas[conta]['Valor']
                        if contas[conta]['Status'] == 'Pago':
                            valorTotalPago += contas[conta]['Valor']

                    # descobrir o quanto um usuário pagou
                    valorTotalUsuario0 = 0
                    for conta in contas:
                        if contas[conta]['Pagante'] == todos[0]:
                            valorTotalUsuario0 += contas[conta]['Valor']

                    # saber o q o outro pagou é valorTotal-valorTotalUsuario0
                    valorTotalUsuario1 = valorTotalPago - valorTotalUsuario0

                    # descobrir a parte que cabe a cada um nas despesas da casa
                    mediaValores = valorTotal / 2
                    mediaValoresPagos = valorTotalPago / 2

                    if opcaofinal == '1':
                        print('##### TOTAL DE DESPESAS #####')
                        print('O total das despesas foi R$ {:.2f}\nFicou R$ {:.2f} para cada pessoa.'.format(valorTotal,
                                                                                                             mediaValores))
                        input('Digite ENTER para continuar ')

                    elif opcaofinal == '2':
                        print('##### DESPESAS CADA USUÁRIO #####')
                        print('{} pagou um total de R$ {:.2f}'.format(todos[0], valorTotalUsuario0))
                        if len(todos) > 1:
                            print('{} pagou um total de R$ {:.2f}'.format(todos[1], valorTotalUsuario1))
                        if valorTotal > valorTotalPago:
                            print('ATENÇÃO! Você tem contas em aberto. Falta cada uma pagar R$ {:.2f}.'
                                  .format((valorTotal - valorTotalPago) / 2))
                        input('Digite ENTER para continuar ')

                    elif opcaofinal == '3':
                        print('##### QUEM DEVE O QUE #####')
                        if len(todos) > 1:
                            valorPagamento = valorTotalUsuario0 - mediaValoresPagos
                            if valorPagamento > 0:
                                print('{} deve pagar R$ {:.2f} a {}'.format(todos[1], abs(valorPagamento), todos[0]))
                            elif valorPagamento < 0:
                                print('{} deve pagar R$ {:.2f} a {}'.format(todos[0], abs(valorPagamento), todos[1]))
                            elif valorPagamento == 0:
                                print('Ninguém ta devendo nada a ninguém.')
                            if valorTotal > valorTotalPago:
                                print('ATENÇÃO! Você tem contas em aberto. Falta cada uma pagar R$ {:.2f}.'
                                      .format((valorTotal - valorTotalPago) / 2))
                            if valorPagamento != 0:
                                # Enviando um e-mail de cobrança
                                questEnviar = input('Quer enviar um e-mail de cobrança? \n► ').lower()
                                while questEnviar != 'sim' and questEnviar != 'não':
                                    questEnviar = input('PQP, digita "sim" ou "não" carai. Anitta sabe...\n► ')
                                if questEnviar == 'sim':
                                    from funcoes_email import sendEmailCobranca

                                    sendEmailCobranca(input('E-mail para envio: '), str(abs(valorPagamento)),
                                                      input('Digite o código do boleto: '))
                                    print('\nE-mail enviado com sucesso!')
                                elif questEnviar == 'não':
                                    print('Tudo bem, mas não esqueça de avisá-la')
                            input('Digite ENTER para continuar ')
                        else:
                            print('Arrume alguém pra dividir as contas!!')
                            input('Digite ENTER para continuar ')




                    elif opcaofinal == '0':
                        break
                    else:
                        print('Opção ínválida')
                        input('Digite ENTER para continuar ')
                # Vai rodar caso CONTAS estiver vazio
                else:
                    print('Você não tem contas cadastradas')
                    input('Digite ENTER para continuar ')
                    break
            # Vai rodas caso TODOS estiver vazio
            else:
                print('Você não tem usuários cadastrados')
                input('Digite ENTER pra continuar ')
                break

    elif escolha1 == '0':
        print('Volte sempre!')
        # Atualizando nossas planilhas com os dados do código
        with open('roomath_contas.csv', 'w', newline='') as csvfile:
            fieldnames = ['Conta', 'Valor', 'Status', 'Pagante']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for conta, infosContas in contas.items():
                writer.writerow({'Conta': conta, 'Valor': infosContas['Valor'],
                                 'Status': infosContas['Status'], 'Pagante': infosContas['Pagante']})

        with open('roomath_perfis.csv', 'w', newline='') as csvfile:
            fieldnames = ['Perfil']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for perfil in todos:
                writer.writerow({'Perfil': perfil})
        break

    else:
        print('Opção ínválida')
        input('Digite ENTER para continuar ')


# ------------------------------------------------------------------------------------------------
# ---------------------------- ENVIANDO E-MAIL -----------------------------------------
# ------------------------------------------------------------------------------------------------
## Aqui é pra se a pessoa quiser enviar um lembrete pra pagar as contas e plau
# from funcoes_email import enviandoLembrete
# #enviandoLembrete()
#

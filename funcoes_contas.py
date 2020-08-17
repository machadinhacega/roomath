def adicionarConta(contas):
    nomeConta = input('Digite o nome da conta que deseja adicionar: ').title()
    valor = input('Valor da conta de {}: '.format(nomeConta))
    #Verificando se o valor digitado pode ser FLOAT
    while True:
        try:
            float(valor)
            break
        except:
            valor = input('Digite um valor válido: ')
    status = input("Qual a situação da conta de {}? (Pago ou Em aberto): ".format(nomeConta)).title()
    #restringindo o status para receber apenas Pago ou Em aberto
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
    input('Digite ENTER para continuar')


def consultarConta(contas):
    if contas:
        consultarConta = input('Digite a conta que deseja consultar: ').title()
        while consultarConta not in contas:
            print(
                'A conta "{}" não esta cadastrada. Escolha uma das contas cadastradas:'.format(consultarConta))
            #Mostrando cada conta registrada
            for k, v in contas.items():
                print(k, end='. ')
            consultarConta = input('\nDigite uma conta válida: ').title()
        print('Dados da conta de {}'.format(consultarConta))
        #Mostrando todos os dados da conta escolhida por chave e valor
        for k, v in contas[consultarConta].items():
            print(k, ': ', v)
        input('Digite ENTER para continuar')
    else:
        print('Você não tem nenhuma conta cadastrada')
        input('Digite ENTER para continuar')


def buscarContaStatus(contas):
    if contas:
        statusBusca = input('Você deseja buscar contas "Pagas" ou "Em aberto"? ').lower()
        while statusBusca != 'pagas' and statusBusca != 'em aberto':
            statusBusca = input('Por favor, digite uma das opções a seguir (Pagas ou Em aberto): ').lower()
            #Mostrando cada conta registrada
            for k, v in contas.items():
                print(k, end='. ')
        #Buscando contas pagas
        if statusBusca == 'pagas':
            print('\nContas Pagas: ')
            #Dentro do dicionario principal esta buscando cada conta(chave) e seu respectivo dicionario(valor)
            for conta, v in contas.items():
                #Dentro de cada dicionário secundario (comentario anterior), está buscando sua chave e seu valor
                for k, v in contas[conta].items():
                    #Verificando apenas a parte que tem escrito "Pago"
                    if v == 'Pago':
                        #Mostrando a conta que tem escrito "Pago"
                        print(conta, end='. ')
        elif statusBusca == 'em aberto':
            #Aqui se repetem os mesmos comentários anteriores da parte "Pagas", mas aplicado aos "Em Aberto"
            print('\nContas Em Aberto: ')
            for conta, v in contas.items():
                for k, v in contas[conta].items():
                    if v == 'Em Aberto':
                        print(conta, end='. ')
        print()
        input('Digite ENTER para continuar')
    else:
        print('Você não tem nenhuma conta cadastrada')
        input('Digite ENTER para continuar')


def editarConta(contas):
    if contas:
        print("dict1 Not Empty")
        nomeConta = input('Digite o nome da conta que deseja Editar: ').title()
        while nomeConta not in contas:
            print('A conta "{}" não esta cadastrada. Escolha uma das contas cadastradas:'.format(nomeConta))
            # Mostrando cada conta registrada
            for k, v in contas.items():
                print(k, end='. ')
            nomeConta = input('\nDigite uma conta válida: ').title()

        print('Dados anteriores da conta de {}'.format(nomeConta))
        # Mostrando os dados atuais da conta registrada
        for k, v in contas[nomeConta].items():
            print(k, ': ', v, end=' | ')
        print('\n')
        valor = input('Novo valor da conta de {}: '.format(nomeConta))
        #Verificando se o valor digitado pode ser FLOAT
        while True:
            try:
                float(valor)
                break
            except:
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
        input('Digite ENTER para continuar')
    else:
        print('Você não tem nenhuma conta cadastrada')
        input('Digite ENTER para continuar')


def excluirConta(contas):
    if contas:
        nomeConta = input('Digite o nome da conta que deseja Excluir: ').title()
        while nomeConta not in contas:
            print('A conta "{}" não esta cadastrada. Escolha uma das contas cadastradas:'.format(nomeConta))
            for k, v in contas.items():
                print(k, end='. ')
            nomeConta = input('\nDigite uma conta válida: ').title()
        contas.pop(nomeConta)
        print('Conta de {} excluída'.format(nomeConta))
        input('Digite ENTER para continuar')
    else:
        print('Você não tem nenhuma conta cadastrada')
        input('Digite ENTER para continuar')


#TESTANTO UM DICIONARIO EXISTENTE
# contas = {'Aluguel': {'Valor': 650.0, 'Status': 'Pago', 'Pagante': 'Iza'}, 'Agua': {'Valor': 59.67, 'Status': 'Pago', 'Pagante': 'Carol'}, 'Internet': {'Valor': 99.9, 'Status': 'Pago', 'Pagante': 'Iza'}}
# adicionarConta(contas)
# consultarConta(contas)
# buscarContaStatus(contas)
# editarConta(contas)
# excluirConta(contas)
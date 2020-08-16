def adicionarUsuario(todos):
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


def editarUsuario(todos):
  editarUsuario = input('Digite o nome do usuário a ser editado: ').title()
  while True:
    if editarUsuario not in todos:
      print('Usuário não cadastrado, escolha um usuário válido:')
      for nome in todos:
        print(nome)
      editarUsuario = input('Informe um usuário cadastrado: ').title()
    else:
      todos.remove(editarUsuario)
      correcaoUsuario = input('Informe um novo nome para {}: '.format(editarUsuario)).title()
      todos.append(correcaoUsuario)
      print(todos)
      break
      while True:
        questEditarUsuario = input('Deseja editar novamente? ').lower()
        if questEditarUsuario == 'sim':
          editarUsuario(todos)
        elif questEditarUsuario == 'não':
          break
        else:
          print('Por favor, digite SIM ou NÃO')

def excluirUsuario(todos):
  print('Lista de perfis:\n', todos)
  while True:
    exUsuario = input('Digite o nome do usuário a ser excluído: ').title()
    if exUsuario not in todos:
      print ('O usuário não foi cadastrado.')
    else:
      todos.remove(exUsuario)
      print ('Lista de usuários atualizada: {}'.format(todos))
      questexUsuario = input('Você deseja excluir outro usuário? ').lower()
      if questexUsuario == 'sim':
        excluirusuario = input('Digite o nome do usuário a ser excluído: ').title()
        todos.remove(excluirusuario)
        print('Lista de perfis atualizada:\n', todos)
      elif questexUsuario == 'não':
        break
      else:
        print('Por favor, digite SIM ou NÃO.')

def adicionarConta(contas):
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

def consultarConta(contas):
  consultarConta = input('Digite a conta que deseja consultar: ').title()
  while consultarConta not in contas:
    print('A conta "{}" não esta cadastrada. Escolha uma das contas cadastradas:'.format(consultarConta))
    for k, v in contas.items():
      print(k, end='. ')
    consultarConta = input('\nDigite uma conta válida: ').title()
  print('Dados da conta de {}'.format(consultarConta))
  for k, v in contas[consultarConta].items():
    print(k, ': ', v)


def statusConta(contas):
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

def editarConta (contas):
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

def excluirConta(contas):
  nomeConta = input('Digite o nome da conta que deseja Editar: ').title()
  while nomeConta not in contas:
    print('A conta "{}" não esta cadastrada. Escolha uma das contas cadastradas:'.format(nomeConta))
    for k, v in contas.items():
      print(k, end='. ')
    nomeConta = input('\nDigite uma conta válida: ').title()
  contas.pop(nomeConta)
  print(contas)
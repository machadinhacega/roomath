# --------------------------------------------------------------------------
# ----------------------  GERENCIAR PERFIL  --------------------------------
# --------------------------------------------------------------------------

def adicionarUsuario(todos):
  while True:
    if len(todos) < 2:
      nomeusuario = input('Digite um nome para adicionar: ').title().strip()
      todos.append(nomeusuario)
      print('Cadastro de {} realizado com sucesso'.format(nomeusuario))
      questNovoUsuario = input('Você gostaria de adicionar mais um perfil? ').lower()
      if questNovoUsuario == 'não':
        break
      elif questNovoUsuario != 'sim' and questNovoUsuario != 'não':
        print('Por favor, digite SIM ou NÃO.')
    else:
      print('Você já tem 2 usuários cadastrados e nosso programa é limitadíssimo')
      input('Digite ENTER para continuar')
      break




def editarUsuario(todos):
# Essa condição verifica se a lista "todos" tem algum elemento nela ou não
  while True:
    if todos:
      editarUsuario = input('Digite o nome do usuário a ser editado: ').title()
      while editarUsuario not in todos:
          print('Usuário não cadastrado, escolha um usuário válido:')
          for nome in todos:
            print(nome)
          editarUsuario = input('Digite o nome do usuário a ser editado: ').title()
      correcaoUsuario = input('Informe um novo nome para {}: '.format(editarUsuario)).title()
      todos.insert(todos.index(editarUsuario), correcaoUsuario)
      todos.remove(editarUsuario)
      print('Usuário atualizado com sucesso.')
      questEditarUsuario = input('Deseja editar novamente? ').lower()
      while questEditarUsuario != 'não' and questEditarUsuario != 'sim':
        questEditarUsuario = input('Por favor, digite SIM ou NÃO \nDeseja editar novamente? ').lower()
      if questEditarUsuario == 'não':
        break
    else:
      print('Você não tem nenhum usuário cadastrado')
      input('Digite ENTER para continuar')



def excluirUsuario(todos):
  while True:
    if todos:
      print('Lista de perfis:\n', todos)
      exUsuario = input('Digite o nome do usuário a ser excluído: ').title()
      while exUsuario not in todos:
        exUsuario = input('O usuário não foi cadastrado. \nDigite o nome do usuário a ser excluído: ').title()
      todos.remove(exUsuario)
      print ('Lista de usuários atualizada')
      questexUsuario = input('Você deseja excluir outro usuário? ').lower()
      while questexUsuario != 'não' and questexUsuario != 'sim':
        questexUsuario = input('Por favor, digite SIM ou NÃO. \nVocê deseja excluir outro usuário? ').lower()
      if questexUsuario == 'não':
        break
    else:
      print('Você não tem nenhum usuário cadastrado')
      input('Digite ENTER para continuar')
      break


# --------------------------------------------------------------------------
# ---------------------  GERENCIAR CONTAS  ---------------------------------
# --------------------------------------------------------------------------

def adicionarConta(contas,todos):
  while True:
    nomeConta = input('Digite o nome da conta que deseja adicionar: ').title()
    valor = input('Valor da conta de {}: '.format(nomeConta))
    # Verificando se o valor digitado pode ser FLOAT
    while True:
      try:
        float(valor)
        break
      except:
        valor = input('Digite um valor válido: ')
    status = input("Qual a situação da conta de {}? (Pago ou Em aberto): ".format(nomeConta)).title()
    # restringindo o status para receber apenas Pago ou Em aberto
    while status != 'Pago' and status != 'Em Aberto':
      status = input("Por favor, digite uma das opções a seguir (Pago ou Em aberto): ").title()
    contas[nomeConta] = {
      'Valor': float(valor),
      'Status': status,
      'Pagante': 'Ninguém pagou ainda :('
    }
    if contas[nomeConta]['Status'] == 'Pago':
      if todos:
        print('Quem pagou a conta? Escolha um dos perfis registrados:')
        for i in todos:
          print(i)
        contas[nomeConta]['Pagante'] = input('► ').title().strip()
        while contas[nomeConta]['Pagante'] not in todos:
          print('Por favor, escolha um perfil registrado')
          for i in todos:
            print(i)
          contas[nomeConta]['Pagante'] = input('Quem pagou a conta: ').title().strip()
      else:
        print('Você não pode adicionar pagantes por que não tem nenhum perfil cadastrado.'
              '\nMas fique tranquile, você pode editar essa conta futuramente.')
    print('Conta de {} adicionada.'.format(nomeConta))
    questAdicionarConta = input('Você deseja adicionar outra conta?  ').lower()
    while questAdicionarConta != 'não' and questAdicionarConta != 'sim':
      questAdicionarConta = input('Por favor, digite SIM ou NÃO. \nVocê deseja excluir outro usuário? ').lower()
    if questAdicionarConta == 'não':
      break


def consultarConta(contas):
  if contas:
    consultarConta = input('Digite a conta que deseja consultar: ').title()
    while consultarConta not in contas:
      print(
        'A conta "{}" não esta cadastrada. Escolha uma das contas cadastradas:'.format(consultarConta))
      # Mostrando cada conta registrada
      for k, v in contas.items():
        print(k, end='. ')
      consultarConta = input('\nDigite uma conta válida: ').title()
    print('Dados da conta de {}'.format(consultarConta))
    # Mostrando todos os dados da conta escolhida por chave e valor
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
      # Mostrando cada conta registrada
      for k, v in contas.items():
        print(k, end='. ')
    # Buscando contas pagas
    if statusBusca == 'pagas':
      print('\nContas Pagas: ')
      # Dentro do dicionario principal esta buscando cada conta(chave) e seu respectivo dicionario(valor)
      for conta, v in contas.items():
        # Dentro de cada dicionário secundario (comentario anterior), está buscando sua chave e seu valor
        for k, v in contas[conta].items():
          # Verificando apenas a parte que tem escrito "Pago"
          if v == 'Pago':
            # Mostrando a conta que tem escrito "Pago"
            print(conta, end='. ')
    elif statusBusca == 'em aberto':
      # Aqui se repetem os mesmos comentários anteriores da parte "Pagas", mas aplicado aos "Em Aberto"
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
    # Verificando se o valor digitado pode ser FLOAT
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
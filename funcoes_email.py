# imports
import smtplib
from email.mime.text import MIMEText


# Enviando um e-mail de cobrança

def sendEmailCobranca (email, valor, boleto):
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
    # username ou email para logar no servidor
    username = 'contatoroomath@gmail.com'
    password = 'desafio#%*694'

    from_addr = 'contatoroomath@gmail.com'
    to_addrs = [email]

    # a biblioteca email possuí vários templates
    # para diferentes formatos de mensagem
    # neste caso usaremos MIMEText para enviar
    # somente texto
    texto = """Olar. Chegou a hora de pagar o que deve ne.
pois então, você ta devendo pra sua roomate"""
    space = ' '
    enter = '\n'
    textoSecundario = 'Pague pelo boleto: '
    message = MIMEText(texto+space+valor+enter+textoSecundario+enter+boleto)
    message['subject'] = 'Bitch, better have my money'
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)

    # conectaremos de forma segura usando SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    # para interagir com um servidor externo precisaremos
    # fazer login nele
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()


# Enviando e-mail de Lembrete

def sendEmailLembrte (email):
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
    username = 'contatoroomath@gmail.com'
    password = 'desafio#%*694'
    from_addr = 'contatoroomath@gmail.com'
    to_addrs = [email]
    texto = """Pague suas contas, meu anjo, se não quiser morar na rua."""
    message = MIMEText(texto)
    message['subject'] = 'Pague suas contas'
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()


# Perguntando se a Pessoa deseja receber um e-mail de Lembrete e rodando a funçao de envio logo em seguida

def enviandoLembrete():
    import datetime
    from time import sleep
    txt = """Você quer que a gnte te lembre de pagar suas contas?
    Sério?
    Você não tem responsabilidade suficiente pra lembrar sozinho?
    Brincadeira. Eu tbm não lembro de tudo.
    Na verdade EU, eu mesma lembro.
    Mas a pessoa que me programou não.
    Então não se sinta culpadi
    Enfim, você quer que eu te lembre?"""

# Aqui eu quis escrever como se estivesse digitando kkkkk

    for i in txt:
        sleep(0.05)
        print(i, end='')

# Perguntando agora real oficial se ela quer

    questEnvio = input('\n► ').lower()
    while questEnvio != 'sim' and questEnvio != 'não':
        questEnvio = input('Mas diga "sim" ou "não" por favor. Não se faça de doido não: ')
    if questEnvio == 'sim':
        diaDoEnvio = input('Qual a data do lembrete?. '
                           '\nO formato é: mm/dd/aa. Coloca no formato certo pfvr.'
                           '\nO FORMATO É ESSE MESMO PQ EU SOU DOENTE\n► ')
        horaDoEnvio = input('E a hora qual é? Mas só a HORA pq eu fiquei com preguiça de fazer bonito'
                            '\nTipo doi numeros. "08" ou "20" por exemplo'
                            '\n► ')
        minutoDoEnvio = input('Agora os minutos pq eu fiquei com preguiça, como ja disse'
                              '\n► ')
        emailEnvio = input('Tem que ter o E-mail, obvio: ')
        txt2 = """Sim, eu vou ficar rodando aqui até enviar
    Por que?
    Eu não tenho mto o que fazer, então decidi ficar aqui esperando.
    ...
    Sim, tou deboas
    Eu quem quise fazer isso
    Sério
    Ta bom, é pq a menina que me pogramou não achou uma forma melhor
    Satisfeiti?
    Só de ruim eu vou atrasar em alguns segundo sua mensagem
    Fodasi o sistema
    Quer dizer
    Não o meu"""
        for i in txt2:
            sleep(0.1)
            print(i, end='')

        while True:
            hoje = datetime.datetime.now()
            hoje = (hoje.strftime("%x"))
            horaAtual = datetime.datetime.now()
            horaHora = (horaAtual.strftime("%H"))
            horaMinuto = (horaAtual.strftime("%M"))
            if diaDoEnvio == hoje and horaDoEnvio == horaHora and minutoDoEnvio == horaMinuto:
                break
        sendEmailLembrte(emailEnvio)
        print('E-mail enviado com Sucesso')

    elif questEnvio == 'não':
        print('\nOk então. Mto responsável você. Parabens. Desculpa ai')
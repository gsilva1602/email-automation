import yagmail
import csv

yag = yagmail.SMTP('youremail', 'yourpassword')

def send_email(destinatario, assunto, conteudo):
    try:
        yag.send(to=destinatario, subject=assunto, contents=conteudo)
        print(f"E-mail enviado para {destinatario}")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

def send_email_personalized(destinatario, nome):
    assunto = f"Testando meu projeto automatizado"
    conteudo = f"Bom dia {nome},\n\nEste é um e-mail automatizado enviado para você feito por mim. Espero que você esteja bem! \n\nAtenciosamente,\nEquipe de Automação"
    send_email(destinatario, assunto, conteudo)

def read_csv(arquivo_csv):
    destinatarios = []
    with open(arquivo_csv, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            destinatarios.append({'email': row['Email'], 'nome': row['Nome']})
    return destinatarios

destinatarios = read_csv('destinatarios.csv')

for d in destinatarios:
    send_email_personalized(d['email'], d['nome'])

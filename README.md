# Automation of sending persolanized e-mails

This project use Python to send e-mails automatic and personalized based in a CSV file that contains the names and e-mails of receivers.

## Tecnologies used
- Python
- Library "yagmail" for send e-mails
- Library "csv" for red csv files

## Features
- Sending automatic e-mails to a receivers list.
- Personalization of e-mail's contents with the name of each receiver.
- Reading receivers from a csv file.

## How to use
1. Clone repository
   ```
   git clone https://github.com/seuusuario/email-automation.git

2. Install dependences
   ```
   pip install yagmail

3. Create a file "destinatarios.csv" in the following format
   ```
   Nome,Email
   João,joao@example.com
   Maria,maria@example.com

4. Execute the script
   ```
   python script.py

## CSV Structure
The CSV file must contain the columns:
- Nome: The receiver name.
- Email: The receiver e-mail.

## Observations
- To use your gmail account, generate an app password and replace in the code.
- Make sure that the access of "less secure apps" be enabled or use an app password for more security.

## Contributions
Feel free to send pull requests or open issues whether have seggestion for improvements.

"""
importações: PANDAS, OPENPYXL, TWILIO
 Passo a Passo

 Abrir os arquivos em Excel

 Para cada arquivo:
 -Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
 -Se for maior do que 55.000 -> Envia um SMS com o nome, o mes e as vendas do vendedor
"""
import pandas as pd
from twilio.rest import Client

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']


for mes in lista_meses:
    tabelas_vendas = pd.read_excel(f'./excel/{mes}.xlsx')
    if (tabelas_vendas['Vendas'] > 55000).any():
        vendedor = tabelas_vendas.loc[tabelas_vendas['Vendas'] > 55000, "Vendedor"].values[0]
        vendas = tabelas_vendas.loc[tabelas_vendas['Vendas'] > 55000, "Vendas"].values[0]
        print(f"O Vendedor: {vendedor} atingiu a margem de vendas: {vendas} no mes: {mes}")

# print(tabela_vendas)



# Your Account SID from twilio.com/console
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309",
    from_="+15017250604",
    body="Hello from Python!")

print(message.sid)
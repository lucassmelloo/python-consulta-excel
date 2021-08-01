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

account_sid = "AC562eba4089e0c5159054c5f6ecc5ffbe"
auth_token = "bac0d7243e8ac4726330d5af78828c85"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']


for mes in lista_meses:
    tabelas_vendas = pd.read_excel(f'./excel/{mes}.xlsx')
    if (tabelas_vendas['Vendas'] > 55000).any():
        vendedor = tabelas_vendas.loc[tabelas_vendas['Vendas'] > 55000, "Vendedor"].values[0]
        vendas = tabelas_vendas.loc[tabelas_vendas['Vendas'] > 55000, "Vendas"].values[0]
        message = client.messages.create(
            to="+5571994090421",
            from_="+14752097481",
            body=f"O Vendedor: {vendedor} atingiu a margem de vendas: {vendas} no mes: {mes}")
        print(message.sid)
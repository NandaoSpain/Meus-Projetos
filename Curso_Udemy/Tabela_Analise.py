import pandas as pd
import win32com.client as win32

# Importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# Visualizar a base de dados
pd.set_option('display.max_columns', None)

# Faturamento por loja
fat_por_loja = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(fat_por_loja)

# Quantidade de produtos vendidos por loja
vendidos_por_loja = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(vendidos_por_loja)

# Ticket médio por loja
ticket_medio = (fat_por_loja['Valor Final'] / vendidos_por_loja['Quantidade']).to_frame()
print(ticket_medio)

# Enviar um email com o relatório
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'To address'
mail.Subject = 'Message subject'
mail.Body = 'Message body'
mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional

# To attach a file to the email (optional):
attachment  = "Path to the attachment"
mail.Attachments.Add(attachment)

mail.Send()
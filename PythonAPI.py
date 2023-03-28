# -*- coding: utf-8 -*-
import requests
import pandas as pd




# AQUI IREMOS CAPTURAR OS CLIENTES 

url1 = 'URL'

# Par�metros da consulta � API
parametros = {
    'page': 1,
    'per_page': 30,
    'api_key': 'KEY'
}

# Cria um DataFrame vazio para armazenar os dados
df2 = pd.DataFrame()

# Loop para obter todas as p�ginas de resultados
while True:

    # Faz uma chamada � API com os par�metros atuais
    response = requests.get(url1, params=parametros)

    # Verifica se a resposta cont�m os dados esperados
    if 'clients' not in response.json():
        break  # Interrompe o loop se n�o houver mais p�ginas

    # Adiciona os dados da p�gina atual ao DataFrame
    dados = response.json()['clients']
    df2 = pd.concat([df2, pd.DataFrame(dados)], ignore_index=True)

    # Atualiza os par�metros de consulta para obter a pr�xima p�gina
    parametros['page'] += 1

    # Imprime o n�mero da p�gina atual
    print(f"CLIENTES INTEGRACAO - Pagina {parametros['page'] - 1} concluida")

    # Interrompe o loop se j� tiver obtido todas as p�ginas
    if len(dados) < parametros['per_page']:
        break

# Seleciona apenas as colunas desejadas
df2 = df2.loc[:, ['id', 'name', 'email', 'address', 'city', 'postal_code', 'fiscal_id', 'country', 'phone']]

# Salva o DataFrame em uma tabela no banco de dados
#df2.to_sql('clientes', con=engine, if_exists='append', index=False)
df2.to_json('clients.json', orient='records', force_ascii=False)



# AQUI COME�O A CAPTURAR OS INVOICES

url = 'https://gabrielalapaunipe.app.invoicexpress.com/invoices.json'

# Par�metros da consulta � API
parametros = {
    'page': 1,
    'per_page': 30,
    'api_key': '637c095a49b0fef977afa0740faaaf81af84b0ee'
}

# Cria um DataFrame vazio para armazenar os dados
df = pd.DataFrame()

# Loop para obter todas as p�ginas de resultados
while True:

    # Faz uma chamada � API com os par�metros atuais
    response = requests.get(url, params=parametros)

    # Verifica se a resposta cont�m os dados esperados
    if 'invoices' not in response.json():
        break  # Interrompe o loop se n�o houver mais p�ginas

    # Adiciona os dados da p�gina atual ao DataFrame
    dados = response.json()['invoices']
    df = pd.concat([df, pd.DataFrame(dados)], ignore_index=True)

    # Atualiza os par�metros de consulta para obter a pr�xima p�gina
    parametros['page'] += 1

    # Imprime o n�mero da p�gina atual
    print(f"VENDAS INTEGRACAO - Pagina {parametros['page'] - 1} concluida")

    # Interrompe o loop se j� tiver obtido todas as p�ginas
    if len(dados) < parametros['per_page']:
        break

# Seleciona apenas as colunas desejadas
df = df.loc[:, ['id', 'status', 'date', 'sum', 'discount', 'before_taxes', 'taxes', 'total', 'currency', 'client', 'items', 'cancel_reason']]

# Salva o DataFrame em um arquivo JSON
df.to_json('Invoices.json', orient='records', force_ascii=False)



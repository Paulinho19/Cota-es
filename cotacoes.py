import requests
import json
#Informa as atuais cotações do dólar, euro e bit-coin
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']['bid']
cotacao_euro = cotacoes['EURBRL']['bid']
cotacao_bit_coin = cotacoes['BTCBRL']['bid']
print('1 dólar vale: R$',cotacao_dolar,'reais!')
print('-'*45)
print('1 euro vale: R$',cotacao_euro,'reais!')
print('-'*45)
print('1 bit-coin vale: R$',cotacao_bit_coin,'reais!')
print('-'*45)

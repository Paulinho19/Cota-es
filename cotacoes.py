import requests
import json
#Informa as atuais cotações do dólar, euro e bit-coin
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = float(cotacoes['USDBRL']['bid'])
cotacao_euro = float(cotacoes['EURBRL']['bid'])
cotacao_bit_coin = float(cotacoes['BTCBRL']['bid'])
print('-'*45)
print('1 dolar vale: R${:.2f} reais!'.format(cotacao_dolar))
print('-'*45)
print('1 euro vale: R${:.2f} reais!'.format(cotacao_euro))
print('-'*45)
print('1 bit-coin vale: R${:.2f} reais!'.format(cotacao_bit_coin))
print('-'*45)

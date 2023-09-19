import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
print(requisicao)

response_data = requisicao.json()
x = float(response_data['USDBRL']['bid'])
print(f"{response_data['USDBRL']['code']} = {x:.2f}")
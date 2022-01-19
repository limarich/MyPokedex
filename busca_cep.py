import requests
busca = input("Digite o nome do lugar ou cep")
api = f"http://cep.la/{busca}"
headers = {"Accept":"application/json"}
lugar = requests.get(api,headers=headers)
print(lugar.json())
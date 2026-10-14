import requests

cep = input("Digite o CEP (apenas números): ")
url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)
status = resposta.status_code
status_str = str(status)

print("Status: " + status_str)

if status == 200:
    dados = resposta.json()
    if "erro" in dados:
        print("CEP não encontrado")
    else:
        print("Bairro: " + dados["bairro"])
        print("Cidade: " + dados["localidade"] + "-" + dados["uf"])
        print("Endereço: " + dados["logradouro"])
else:
    print("CEP com formato inválido")

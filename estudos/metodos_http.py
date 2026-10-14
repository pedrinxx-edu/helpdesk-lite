import requests
contagem = 1

url_lista = "https://jsonplaceholder.typicode.com/posts"
url = "https://jsonplaceholder.typicode.com/posts/1"

resposta_lista = requests.get(url_lista)
resposta = requests.get(url)

dados_lista = resposta_lista.json()
dados = resposta.json()

print(f"Foram registradas {len(dados_lista)} publicações")
print("Dentre elas: ")
for publicacao in dados_lista:
    print(f"{contagem} - {publicacao['title']}")
    contagem += 1

print(f"Mas da url comum, só veio este titulo de publicação: {dados['title']}")
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

nova_publicacao = {"title": "Naruto", "body": "Naruto era uma criança sozinha e tristonha", "userId": 1}
resposta_post = requests.post(url_lista, json=nova_publicacao)

print(resposta_post.status_code)
dados_post = resposta_post.json()
id = str(dados_post['id'])
print(id + " - " + dados_post['title'])
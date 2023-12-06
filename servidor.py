from socket import socket, AF_INET, SOCK_DGRAM
from datetime import datetime

with open('./files/index.html', 'r') as f:
    index_html = f.read()
with open('./files/style.css', 'r') as f:
    style_css = f.read()

def print_and_save_in_file(text: str):
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    textoServidor = f'[SERVIDOR - {data}] {text}'
    print(textoServidor)
    with open("log.txt", "a") as file:
        file.write('\n----------\n')
        file.write(textoServidor) 

socket_servidor = socket(AF_INET, SOCK_DGRAM)

socket_servidor.bind(('127.0.0.1', 10311))

print_and_save_in_file("Servidor iniciado, aguardando conexoes...")

while True:
    data, addr = socket_servidor.recvfrom(2048)
    print_and_save_in_file(f"Conexao estabelecida com {addr}")

    request = data.decode()
    if not request:
        print_and_save_in_file(f"Nenhuma requisição foi enviada, conexao fechada com {addr}")
        break
    
    print_and_save_in_file(f"Requisicao recebida de: {addr}\n {request}")

    if request.startswith('GET / HTTP/1.1'):
        reply = 'HTTP/1.1 200 OK\n\n' + index_html
    elif request.startswith('GET /style.css HTTP/1.1'):
        reply = 'HTTP/1.1 200 OK\n Content-Type: text/css\n\n' + style_css
    else:
        reply = 'HTTP/1.1 404 Not Found\n\nPage not found.'

    print_and_save_in_file(f"Resposta enviada para: {addr}\n {reply}")
    socket_servidor.sendto(reply.encode(), addr)

print_and_save_in_file(f"Conexao fechada com o {addr}")
socket_servidor.close()
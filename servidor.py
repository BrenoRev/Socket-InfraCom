from socket import socket, AF_INET, SOCK_STREAM;
from threading import Thread

def processa_requisicao(socket_cliente):
    for _ in range(2):
        requisicao = socket_cliente.recv(2048)
        mensagem = requisicao.decode()
        print(f'A requisição do cliente foi {mensagem}')
        resposta = "Ola, cliente"
        socket_cliente.send(resposta.encode())

socket_servidor = socket(AF_INET, SOCK_STREAM)

socket_servidor.bind(('127.0.0.1', 12345))

socket_servidor.listen()

for i in range(2):

    socket_cliente, endereco_cliente = socket_servidor.accept()

    print(f'O cliente {endereco_cliente} estabeleceu uma conexão...')

    Thread(target=processa_requisicao, args=(socket_cliente,)).start()

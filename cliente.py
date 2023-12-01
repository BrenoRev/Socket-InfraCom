from socket import socket, AF_INET, SOCK_STREAM

socket_cliente = socket(AF_INET, SOCK_STREAM)

socket_cliente.connect(('127.0.0.1', 12345))

for _ in range(2):
    mensagem = input('>>>>>')

    requisicao = mensagem.encode()

    socket_cliente.send(requisicao)

    resposta = socket_cliente.recv(2048)

    print(f'A resposta recebida foi {resposta.decode()}')
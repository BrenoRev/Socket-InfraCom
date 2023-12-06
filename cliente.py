from socket import socket, AF_INET, SOCK_STREAM
from datetime import datetime

MAX_REQUEST_PER_CONNECTION = 5

def print_and_save_in_file(text: str):
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    textoCliente = f'[CLIENTE - {data}] {text}'
    print(textoCliente)
    with open("log.txt", "a") as file:
        file.write('\n----------\n')
        file.write(textoCliente)

socket_cliente = socket(AF_INET, SOCK_STREAM)

socket_cliente.connect(('127.0.0.1', 10311))

for _ in range(MAX_REQUEST_PER_CONNECTION):
    mensagem = input("Insira o texto: ")

    print_and_save_in_file(f"Enviando requisicao:\n {mensagem}")

    requisicao = mensagem.encode()

    socket_cliente.send(requisicao)

    resposta = socket_cliente.recv(2048)

    print_and_save_in_file(f'A resposta recebida foi:\n {resposta.decode()}')
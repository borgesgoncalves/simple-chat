import socket

# Criando um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Vinculando o socket ao endereço e porta
server_socket.bind(('localhost', 12345))

# Escutando por conexões
server_socket.listen(5)
print("Conected")

# Aceitando conexões de clientes
while True:
    conn, addr = server_socket.accept()

    print(f"Connected at {addr}")
    while True:
        # Recebendo mensagem do cliente
        data = conn.recv(1024)
        if not data:
            break
        print(f"Message received: {data.decode()}")

        # Respondendo ao cliente
        if data.decode() == "Hey, server":
            conn.sendall(b"Hey, client")
        elif data.decode() == "Exit":
            conn.sendall(b"Closing connection")
            conn.close()
            break
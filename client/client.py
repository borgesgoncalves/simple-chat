import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando ao servidor
client_socket.connect(('localhost', 12345))

# Enviando um mensagem para o servidor
while True:
   message = input("Type your message: ")
   client_socket.sendall(message.encode())
   if message == "Exit":
      client_socket.close()
      break
   # Recebendo resposta do servidor
   data = client_socket.recv(1024)
   print(f"Server: {data.decode()}")
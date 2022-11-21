import socket
import getpass
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost",9999))
massage = client.recv(1024).decode()
client.send(input(massage).encode())
massage = client.recv(1024).decode()
client.send(getpass.getpass(massage).encode())
print(client.recv(1024).decode())

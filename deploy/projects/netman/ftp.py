


global socket, handle_client

import socket
import os

def handle_client(client_socket):
    client_socket.send("220 Welcome to Minimal FTP Server\r\n".encode())
    
    while True:
        request = client_socket.recv(1024).decode().strip()
        if not request:
            break
        
        if request == "QUIT":
            client_socket.send("221 Goodbye.\r\n".encode())
            break
        
        if request.startswith("LIST"):
            files = os.listdir('.')
            file_list = '\r\n'.join(files)
            client_socket.send(f"150 Here comes the directory listing.\r\n{file_list}\r\n226 Directory send OK.\r\n".encode())
        else:
            client_socket.send("500 Command not supported.\r\n".encode())
    
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8081))
    server_socket.listen(5)
    print("FTP Server listening on port 8081...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()
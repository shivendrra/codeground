import socket
from datetime import datetime

def handle_client(client_socket):
  request = client_socket.recv(1024).decode('utf-8')
  print(f"Received request:\n{request}")

  response = "HTTP/1.1 200 OK\r\n"
  response += "Content-Type: text/html\r\n"
  response += "\r\n"
  response += f"<html><body><h1>Hello, World!</h1><p>Current time: {datetime.now()}</p></body></html>"

  client_socket.sendall(response.encode('utf-8'))
  client_socket.close()

def main():
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  server_socket.bind(('0.0.0.0', 8080))
  server_socket.listen(5)

  print("Server is listening on port 8080...")

  while True:
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")
    handle_client(client_socket)

if __name__ == "__main__":
  main()
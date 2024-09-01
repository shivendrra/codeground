#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h>

#pragma comment(lib, "ws2_32.lib")

int main() {
  WSADATA wsa;
  SOCKET server_socket, client_socket;
  struct sockaddr_in server, client;
  int c;
  char *message, client_reply[2000];

  printf("Initializing Winsock...\n");
  if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) {
    printf("Failed. Error Code: %d\n", WSAGetLastError());
    return 1;
  }
  printf("Winsock initialized.\n");

  if ((server_socket = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET) {
    printf("Could not create socket. Error Code: %d\n", WSAGetLastError());
    return 1;
  }
  printf("Socket created.\n");

  server.sin_family = AF_INET;
  server.sin_addr.s_addr = INADDR_ANY;
  server.sin_port = htons(8080);

  if (bind(server_socket, (struct sockaddr *)&server, sizeof(server)) == SOCKET_ERROR) {
    printf("Bind failed. Error Code: %d\n", WSAGetLastError());
    return 1;
  }
  printf("Bind done.\n");

  listen(server_socket, 3);
  printf("Waiting for incoming connections...\n");

  c = sizeof(struct sockaddr_in);
  while ((client_socket = accept(server_socket, (struct sockaddr *)&client, &c)) != INVALID_SOCKET) {
    printf("Connection accepted.\n");

    memset(client_reply, 0, sizeof(client_reply));
    int recv_size = recv(client_socket, client_reply, 2000, 0);
    if (recv_size == SOCKET_ERROR) {
      printf("Recv failed. Error Code: %d\n", WSAGetLastError());
      break;
    }
    printf("Received HTTP request:\n%s\n", client_reply);

    message = "HTTP/1.1 200 OK\r\n"
              "Content-Type: text/html\r\n"
              "Connection: close\r\n"
              "\r\n"
              "<html><body><h1>Hello, World!</h1></body></html>";
    send(client_socket, message, strlen(message), 0);
    printf("HTTP response sent.\n");

    closesocket(client_socket);
    printf("Connection closed.\n");
  }

  if (client_socket == INVALID_SOCKET) {
    printf("Accept failed. Error Code: %d\n", WSAGetLastError());
  }

  closesocket(server_socket);
  WSACleanup();
  return 0;
}
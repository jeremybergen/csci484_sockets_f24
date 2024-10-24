#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int socketNum, clientSocket;
    int bindStatus, listenStatus;
    int yes = 1;
    struct sockaddr_in address;
    struct sockaddr_in clientAddress;
    int addrSize = sizeof(struct sockaddr_storage);

    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_family = AF_INET;
    address.sin_port = htons(1234);

    socketNum = socket(AF_INET, SOCK_STREAM, 0);
    setsockopt(socketNum, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(yes));
    bindStatus = bind(socketNum, (struct sockaddr *)&address, sizeof(address));
    listenStatus = listen(socketNum, 5);


    printf("Socket: %d\n", socketNum);
    printf("bindStatus: %d\n", bindStatus);
    printf("listenStatus: %d\n", listenStatus);

    clientSocket = accept(socketNum, (struct sockaddr *)&address, (socklen_t *)&addrSize);

    printf("clientSocket: %d\n", clientSocket);
    char* buffer;
    malloc(buffer, 1024);
    recv(clientSocket, buffer, 1024, 0);
    printf("Received: %s\n", buffer);
    // while(1)
    // {

    // }
    return 0;
}
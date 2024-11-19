import socket
import select

def main():
    IP = "127.0.0.1"
    PORT = 1234
    HEADERLENGTH=10

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serverSocket.bind((IP, PORT))

    serverSocket.listen()

    socketList = [serverSocket]
    clients = {}
    print(f"Listening for connections on {IP}:{PORT}")
    while True:
        readSockets, _, exceptionSockets = select.select(socketList, [], socketList)
        for notifiedSocket in readSockets:
            if notifiedSocket == serverSocket:
                clientSocket, clientAddress = serverSocket.accept()

                socketList.append(clientSocket)
                usernameHeader = clientSocket.recv(HEADERLENGTH)
                usernameLength = int(usernameHeader.decode().strip())
                username = clientSocket.recv(usernameLength)
                clients[clientSocket] = username.decode()
                print(f"Accepted new connection from {clientAddress}, username: {clients[clientSocket]}")
            else:
                # message = notifiedSocket.recv(1024)
                # usernameHeader = clientSocket.recv(HEADERLENGTH)
                # usernameLength = int(usernameHeader.decode().strip())
                # username = clientSocket.recv(usernameLength).decode()
                user = clients[notifiedSocket]
                print(f"DEBUG: clients[notifiedSocket]: {clients[notifiedSocket]}")

                # print(f"username: {username}")

                messageHeader = clientSocket.recv(HEADERLENGTH)
                print(f"messageHeader: {messageHeader}")
                messageLength = int(messageHeader.decode().strip())
                print(f"messageLength: {messageLength}")
                recvMessage = clientSocket.recv(messageLength).decode()
                print(f"message: {recvMessage}")
                print(f"user: {user}")
                # print(f'message: {message["data"]}')
                print(f'Received message from {user}: {recvMessage}')
                for clientSocket in clients:
                    if clientSocket != notifiedSocket:
                        clientSocket.send(f"{len(user):<{HEADERLENGTH}}{user}{len(recvMessage):<{HEADERLENGTH}}{recvMessage}".encode())

    serverSocket.close()


if __name__ == "__main__":
    main()
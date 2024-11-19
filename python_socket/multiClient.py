import socket
import select
import errno
import sys

def main():
    IP = "127.0.0.1"
    PORT = 1234
    HEADERLENGTH = 10

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    clientSocket.connect((IP, PORT))
    clientSocket.setblocking(False)

    username = input("Enter a username: ")
    # print(f"'{len(username):<{HEADERLENGTH}}'")
    # sys.exit()
    clientSocket.send(f"{len(username):<{HEADERLENGTH}}{username}".encode())

    while True:
        message = input(f"{username}: ")
        if message:
            # clientSocket.send(message.encode())
            print(f"DEBUG: Sending '{len(message):<{HEADERLENGTH}}{message}'")
            clientSocket.send(f"{len(message):<{HEADERLENGTH}}{message}".encode())

        try:
            while True:
                # recvMessage = clientSocket.recv(1024)
                usernameHeader = clientSocket.recv(HEADERLENGTH)
                usernameLength = int(usernameHeader.decode().strip())
                recvUsername = clientSocket.recv(usernameLength).decode()

                messageHeader = clientSocket.recv(HEADERLENGTH)
                messageLength = int(messageHeader.decode().strip())
                recvMessage = clientSocket.recv(messageLength).decode()

                print(f"{recvUsername}: {recvMessage}")
                # recvMessage = recvMessage.decode()
                # print(f"Received: {recvMessage.decode()}")
                # recvUsername = 
        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print(f"reading error: {str(e)}")
                sys.exit()
            continue

if __name__ == "__main__":
    main()
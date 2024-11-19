import socket as so
from socket import socket

def main():
    host = "127.0.0.1"
    port = 1234
    with socket(so.AF_INET, so.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        # print("Client connected from: {}".format(addr))
        # print("Client connected from:", addr)
        print(f"Client connected from: {addr}")

        while True:
            data = conn.recv(1024)
            print(f"Received from client: {data}")
            # conn.send(data)
            if not data:
                break
            conn.sendall(data)

        # conn.close()

if __name__ == "__main__":
    main()
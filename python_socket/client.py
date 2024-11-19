import socket

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cs:
        cs.connect(("127.0.0.1", 1234))
        cs.sendall(b"Hello World")
        data = cs.recv(1024)
        print(f"Received from server: {data}")


if __name__ == "__main__":
    main()
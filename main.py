import socket

if __name__ == "__main__":
    socket_desc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_desc.connect(('127.0.0.1', 1234))
    while True:
        try:
            request = input('Request: ').encode()
            socket_desc.send(request)
            response = socket_desc.recv(1024)
            print(response.decode())
        except KeyboardInterrupt:
            break
    socket_desc.close()
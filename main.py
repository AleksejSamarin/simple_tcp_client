import socket

if __name__ == "__main__":
    socket_desc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_desc.connect(('127.0.0.1', 1234))
    while True:
        try:
            request = input('Request (ANSI): ').encode('ansi') # формирование сообщения для сервера с кодировкой ANSI
            socket_desc.send(request)
            response = socket_desc.recv(1024)
            print(f"Response (ASCII): {response.decode('ascii')}") # принятие сообщения от сервера с кодировкой ASCII
        except KeyboardInterrupt:
            break
    socket_desc.close()
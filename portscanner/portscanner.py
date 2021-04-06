import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print('\n [ Scanning Target ] ', target)
    for port in range (1, 500):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner():
    sock = socket.socket()
    return sock.recv(6144)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print("[~] Port ", port, "Is Open and Currently running:", banner.decode().strip('\n'))
        except:
            print(f'[~] Port {port} is Open')
    except:
        pass


if __name__ == '__main__':
    targets = input(f'[~] Enter Target(s) To Scan (Split Multiple Targets with comma(,)): ')
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip())
    else:
        scan(targets)
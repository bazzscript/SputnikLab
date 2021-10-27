import portscanner

targets_ip = input('[~] Enter Target(s) To Scan (Split Multiple Targets with comma(,)): ')

while True:
    try:
        port_number = int(Input('[~] Enter Amount of Ports you want to Scan(500 means first 500 ports) : '))
        break
    except ValueError:
        print(' We dont understand what you typed \nTry Again...\nPlease A number')

#vul_soft_list = input("[~] Enter Path To the list of vulnerble softwares : ")
#target = portscabber.PortScan(targets_ip, port_number)
#target.scan()

#targets = input(f '[~] Enter Target(s) To Scan (Split Multiple Targets with comma(,)): ')

if ',' in targets_ip:
    for ip_add in targets_ip.split(','):
        target = portscanner.PortScan(ip_add.strip(), port_number)
        target.scan()
else:
    target = portscanner.PortScan(targets_ip, port_number)
    target.scan()

while True:
    try:
        vul_soft_list = input("[~] Enter Path To the txt list of names vulnerable softwares : ")
        with open(vul_soft_list, 'r') as file:
            count = 0
            for banner in target.banners:
                file.seek(0)
                for line in file.readlines():
                    if line.strip() in banner:
                        print('\n\n')
                        print('[!!!] VULNERABLE SOFTWARE "', banner, '"DETECTED ON PORT: ', str(target.open_ports[count]))
                count += 1
        break
    except FileNotFoundError as e:
        print('[!!] That File/Path doesnt\'t exists ')
        print('Try Again')
import nmap

scanner = nmap.PortScanner()

print('Welcome, This is a simple nmap automation tool')
print('----------------------------------------------')

ip_adr = input('Please enter the IP address you want to scan: ')

print('The IP you entered is: ',ip_adr)
type(ip_adr)

resp = input("""\n Please enter the type of scan you want to run
             1) SYN-ACK Scan
             2) UDP Scan
             3) Comprehensive Scan\n""")
print('You choose the option: ',resp)

if resp == '1':
    print('Nmap version: ',scanner.nmap_version())
    scanner.scan(ip_adr,'1-1024','-v -sS')
    print(scanner.scaninfo())
    print("IP status: ",scanner[ip_adr].state())
    print(scanner[ip_adr].all_protocols())
    print('Open Ports: ',scanner[ip_adr]['tcp'].keys())

elif resp == '2':
    print('Nmap version: ',scanner.nmap_version())
    scanner.scan(ip_adr,'1-1024','-v -sU')
    print(scanner.scaninfo())
    print("IP status: ",scanner[ip_adr].state())
    print(scanner[ip_adr].all_protocols())
    print('Open Ports: ',scanner[ip_adr]['udp'].keys())

elif resp == '3':
    print('Nmap version: ',scanner.nmap_version())
    scanner.scan(ip_adr,'1-1024','-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP status: ",scanner[ip_adr].state())
    print(scanner[ip_adr].all_protocols())
    print('Open Ports: ',scanner[ip_adr]['tcp'].keys())

else:
    print('Please enter a valid option...')
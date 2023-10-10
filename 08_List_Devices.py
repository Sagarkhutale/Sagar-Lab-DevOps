import paramiko
import time
from getpass import getpass

# ip = input('Enter IP: ')
username = 'admin'
password = 'admin'

Device_List = ['192.168.122.' +str(n) for n in range(10,14)]

for RTR in Device_List:
    print('\n ####### Connecting to the Device ' + RTR + '#####\n')
    Session = paramiko.SSHClient()
    Session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    Session.connect(RTR, username=username, password=password, port=22, look_for_keys=False,allow_agent=False)

    SSH_Access = Session.invoke_shell()
    SSH_Access.send (b'config t\n')
    for N in range (1,5):
        SSH_Access.send('int loopback '+str(N) + '\n')
        SSH_Access.send('ip address 1.1.1.' +str(N) + ' 255.255.255.255\n')

    time.sleep(3)        
    SSH_Access.send(b'do terminal len 0\n')
    SSH_Access.send(b'do show version\n')
    SSH_Access.send(b'do show ip int bri\n')

    time.sleep(2)
    output = SSH_Access.recv(65000)
    print(output.decode('utf-8'))

    Session.close()
import paramiko
import time
from getpass import getpass

ip = input('Enter IP: ')
username = input('Enter username: ')
password = input('Enter Password: ')
a = int (input('Enter the first Loopback in range : '))
b = int (input('Enter the last Loopback in range : ')) + 1

Session = paramiko.SSHClient()
Session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
Session.connect(ip, username=username, password=password, port=22, look_for_keys=False,allow_agent=False)

SSH_Access = Session.invoke_shell()
SSH_Access.send (b'config t\n')

for N in range (a,b):
    SSH_Access.send('no int loopback '+str(N) + '\n')
    #SSH_Access.send('ip address 1.1.1.' +str(N) + ' 255.255.255.255\n')

time.sleep(3)        
SSH_Access.send(b'do terminal len 0\n')
SSH_Access.send(b'do show version\n')
SSH_Access.send(b'do show ip int bri\n')

time.sleep(2)
output = SSH_Access.recv(65000)
print(output.decode('utf-8'))

Session.close()

import paramiko
import time
from getpass import getpass

ip = input('Enter IP: ')
username = input('Enter username: ')
password = input('Enter Password: ')

Session = paramiko.SSHClient()
Session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
Session.connect(ip, username=username, password=password, port=22, look_for_keys=False,allow_agent=False)

SSH_Access = Session.invoke_shell()
SSH_Access.send(b'terminal len 0\n')
SSH_Access.send(b'show version\n')
time.sleep(2)
output = SSH_Access.recv(65000)
print(output.decode('utf-8'))

Session.close()
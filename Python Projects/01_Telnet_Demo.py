from telnetlib import Telnet
tn = Telnet('192.168.122.10') 
tn.write(b"admin\r\n")
tn.write(b"admin\r\n")
tn.write(b'term length 0\r\n')
cmd = input('enter the command: ')
#tn.write(cmd + '\n')
tn.write(b'show version\r\n')
tn.write(b'exit\n')
output = tn.read_all().decode("utf-8")
print(output)


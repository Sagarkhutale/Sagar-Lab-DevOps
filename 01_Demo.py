import getpass
from telnetlib import Telnet
import sys
import time

HOST = "192.168.122.10"
user = input("Enter your remote account: ")
#user = user.rstrip()
password = getpass.getpass()

tn = Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
time.sleep(1)
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    time.sleep(1)

#tn.write(b"ls\r\n")
tn.write(b"term length 0\n")
tn.write(b"show version\n")
tn.write(b"show ip int bri\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
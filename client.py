
"""
Author : Eric Muli
Github : github.com/EricRootLee
Page Title : Client Side Code
Platform : Any Os
Target : N/A
Technology : Python
"""


from socket import socket ,AF_INET,SOCK_DGRAM

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('localhost'  ,6667)) ####receiver

def receive_msg():
        while True:
                msg , addr = sock.recvfrom(8192)####sender
                print("Got Msg from %s: %s:"%(addr, msg) )
                if len(msg):
                        send_msg()

def send_msg():
        while True:
                user_input = input(str("Type Your Text:"))
                msg = user_input.encode('utf-8')
                sock.sendto(msg,('localhost',8192),)
                             
                receive_msg()

send_msg()

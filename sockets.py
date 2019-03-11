
from socket import  socket ,AF_INET,SOCK_DGRAM

s = socket(AF_INET,SOCK_DGRAM)
s.bind(('localhost'  ,8192)) 

def send_msg():
    while True:
        user_input = input(str("Type Your Text:"))
        msg = user_input.encode('utf-8')
        s.sendto(msg,('localhost',6667),)
        receive_msg()

def receive_msg():
    while True:
        msg , addr = s.recvfrom(8192)####sender      
        print("Got Msg from %s: %s:"%(addr, msg))       
        if len(msg) > 0:
               send_msg()
               
send_msg()
   
import socket
# import socket module/library to create
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#what is my receiver address
recv_addr=("127.0.0.1",9999)
# now i want to send message
user_data=input("enter your message :-")
# now you can send data
newdata=user_data.encode('ascii')
print("your mesage has been send..")
s.sendto(newdata,recv_addr)


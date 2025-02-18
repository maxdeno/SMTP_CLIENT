import base64
import socket
import ssl


# smtp server
mail_server = "smtp.gmail.com"
port = 587

# sender's credentials

sender_email = "denomax517@gmail.com"
encoded_sender_email = base64.b64encode(sender_email.encode()).decode()
sender_password = "kavt ecli axfi blax"
encoded_sender_password = base64.b64encode(sender_password.encode()).decode()
recipient_email = "grugermax69@gmail.com"
encoded_recipient_email = base64.b64encode(sender_password.encode()).decode()


#   send message
email_body = """\
From: denomax517@gmail.com
To: grugermax69@gmail.com
Subject: SMTP CLIENT TEST EMAIL
MIME-Version: 1.0
Content-Type: text/plain; charset="UTF-8"
                        
Hey,
I am Dennis Kithinji aka Soja35, This message is from a simple coded python SMTP client.
It's good progress, learning networking while coding. 
                        
yours truly,
Dennis(soja35)
"""

print("[DEBUG] sending email body...")
print(email_body)


# create a socket and connect the mail
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((mail_server, port))
recv = client_socket.recv(1024).decode()
print(recv)

if recv[:3] != "220":
    print("220 reply not received from the server")


# send the helo command(handsheking)
ehlocommand = "EHLO Dennis\r\n"
client_socket.send(ehlocommand.encode())
recv1 = client_socket.recv(1024).decode()
print(recv1)

if recv1[:3] != "250":
    print("250 reply  not received from the server!")


# request to upgrade to TLS
client_socket.send("STARTTLS\r\n".encode())
recv2 = client_socket.recv(1024).decode()
print(recv2)


# secure connection using ssl
context = ssl.create_default_context()
client_socket = context.wrap_socket(client_socket, server_hostname=mail_server)

# send the EHLO command again
client_socket.send(ehlocommand.encode())
recv3 = client_socket.recv(1024).decode()
print(recv3)

# send Auth login command
client_socket.send("AUTH LOGIN\r\n".encode())
recv4 = client_socket.recv(1024).decode()
print(recv4)

# encoding the sender's credentials
client_socket.send((encoded_sender_email + "\r\n").encode())
recv5 = client_socket.recv(1024).decode()
print(recv5)


client_socket.send((encoded_sender_password + "\r\n").encode())
recv6 = client_socket.recv(1024).decode()
print(recv6)


# send the MAIL  command
client_socket.send(f"MAIL FROM: <{sender_email}>\r\n".encode())
recv7 = client_socket.recv(1024).decode()
print(recv7)


# send the RCPT command
rcpt_to_command = (f"RCPT TO: <{recipient_email}>\r\n")
client_socket.send(rcpt_to_command.encode())
recv8 = client_socket.recv(1024).decode()
print(recv8)


# send  DATA command
client_socket.send("DATA\r\n".encode())
recv9 = client_socket.recv(1024).decode()
print(recv9)


# send the message data
client_socket.send(email_body.encode())
client_socket.send("\r\n.\r\n".encode())
recv10 = client_socket.recv(1024).decode()
print("[DEBUG] server response after sending the message:", recv10)


# send the QUIT command
client_socket.send("QUIT\r\n".encode())
recv11 = client_socket.recv(1024).decode()
print(recv11)

# close the connection
client_socket.close()

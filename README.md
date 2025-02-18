# SMTP_CLIENT

#🎯 Task
Develop a simple mail client that sends email to any recipient. Your client will need to
connect to a mail server, dialogue with the mail server using the SMTP protocol, and send an email
message to the mail server.

# Factors considered:
1. Mail server: Smtp.gmail.com  used.
2. Authentication: using the app password feature in the google's gmail.<br>
   The app password enables simple mail client to authenticated by the smtp server.<br>
3. Firewall and network settings.
   The smtp port 25 can't be used due to its restrctions.<br>
   check if the network or firewall allows traffic through the smtp ports, i.e port 587, 425.<br>
   use mobile network, vpn or change the firewall rule to allow traffic.<br>

# Action Plan
1. Establish a TCP connection to smtp.gmail.com on port 587.<br>
2. Perform SMTP handshake(EHLO, MAIL FROM, RCPT TO).<br>
3. Upgrade the connection to Transport Layer Security, and encrpyt the connection in secure socket layer.  Makes the coonection more secure.<br>
4. Authenticate the SMTP Client using encoded Base64 credentials.<br>
5. Send the message.<br>
6. close the connection and quit the session.<br>

# Operation
The smtp client connects with the smtp server, performing authentication to enhance the connection. Once the connection is established, the server and client perform a handshake i.e EHLO, MAIL TO, RCPT TO commands. After the handshaking process is completed, the client sends the email body to the server and the server forwards it to the recipient's email address.

# Status code:
2xx(Success)<br>
220 - server is ready for coonection.<br>
250 - Action initiated by the smtp client has been accepted by the server.<br>
235 - Authentication successful.<br>
221 - server closing the connection.<br>

3xx(Immediate response)<br>
334 - server requesting for authentication details.<br>
335 - server ready to receive email.<br>

4xx(Temporary Failure)<br>
421 -	Service unavailable (server shutting down)<br>
450 - Mailbox unavailable (e.g., user’s inbox is full)<br>
451 -	Server error (e.g., temporary server issue)<br>
452 -	Too many emails sent (server has rate limits)<br>

5xx(Permanent Failure)<br>
500 - Syntax error (invalid command)<br>
501 -	Invalid email address<br>
503 -	Incorrect command sequence (e.g., sending MAIL FROM before HELO)<br>
550 -	Email not delivered (recipient address doesn't exist)<br>
554 -	Message rejected (e.g., spam detected)<br>


SMTP backend status:
![Image](https://github.com/user-attachments/assets/49e932bf-f6db-4511-8037-03cba0d21c89)

Recipient email inbox:
![Image](https://github.com/user-attachments/assets/5980c99e-683c-45dc-8b90-e0365e2e4549)






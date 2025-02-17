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


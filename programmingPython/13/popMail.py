import poplib, sys

mailServer = "pop3.163.com"
mailUser = "18719091650@163.com"
mailPasswd = "5201314ouru..."

print "connection...."
server = poplib.POP3(mailServer)
server.user(mailUser)
server.pass_(mailPasswd)

try:
    print server.getwelcome()
    msgCount, msgBytes = server.stat()
    print "There are", msgCount, "mail message in", msgBytes, "bytes"
    print server.list()
    print "-" * 80
    raw_input("Press Enter key")
    for i in range(1):
        hdr, message, octest = server.retr(i + 1)
        for line in message:
            print line
        print "-" * 80
finally:
    server.quit()

print "Bye."
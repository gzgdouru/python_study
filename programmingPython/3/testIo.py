from io import StringIO

buff = StringIO()

print buff.write(u"spam\n")
print buff.write(u"eggs\n")

print buff.getvalue()

buff = StringIO(u"ham\nspam\n")
print str(buff.readline()).rstrip()
print buff.readline().rstrip()
print buff.readline()

print "-" * 50

from io import BytesIO
stream = BytesIO()
stream.write(b"spam")
print stream.getvalue()
stream = BytesIO(b"hello")
print stream.read()
print stream.read()

print "hello",
print "word"
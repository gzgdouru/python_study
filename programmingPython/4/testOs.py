import os

info = os.stat("spam.txt")
print info

print info.st_size

print os.path.getsize("spam.txt")
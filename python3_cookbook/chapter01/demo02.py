'''
解压可迭代对象赋值给多个变量
'''

if __name__ == "__main__":
    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    name, email, *phones = record
    print(name, email, phones)

    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    uname, *fields, homedir, sh = line.split(":")
    print(uname, homedir, sh)

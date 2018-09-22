import time

print time.time()
print time.localtime()

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

time.sleep(1)

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

strDate = "2017-10-30"
date = time.strptime(strDate, "%Y-%m-%d")
print date.tm_yday

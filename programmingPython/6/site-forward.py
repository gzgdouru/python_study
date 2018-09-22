import os

serverName = "learning-python.com"
homeDir = "books"
siteFilesDir = r""
uploadDir = r""
templateName = "template.html"

try:
    os.mkdir(uploadDir)
except OSError:
    pass

template = open(templateName).read()
sitesFiles = os.listdir(siteFilesDir)

count = 0
for fileName in sitesFiles:
    if str(fileName).endswith("html") or str(fileName).endswith("htm"):
        fwdName = os.path.join(uploadDir, fileName)
        print "creating", fileName, "as", fwdName
        fileText = template.replace("$server$", serverName)
        fileText = fileText.replace("$home$", homeDir)
        fileText = fileText.replace("$file$", fileName)
        open(fwdName, "w").write(fileText)
        count += 1

print "Last file=>\n", fileText,
print "Done:", count, "forward file create."
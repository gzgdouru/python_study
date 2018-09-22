import sys
from scanfile import scanner

class UnknownCommand(Exception):
    pass


commands = {"*" : "Ms.", "+" : "Mr."}

def processLine(line):
    try:
        print "%s%s" % (commands[line[0]], line.rstrip())
    except KeyError:
        raise UnknownCommand(line)


fileName = "data.txt" if len(sys.argv) != 2 else sys.argv[1]
scanner(fileName, processLine)
import sys

def filter_files(name, func):
    input = open(name)
    output = open(name + ".out", "w")
   #output.write(map(func, [str(line) for line in input]))
    #for line in input:
        #output.write(func(line))
    map(output.write, map(func, [line for line in input]))

def filter_stream(func):
    for line in sys.stdin:
        #line = sys.stdin.readline()
        #if not line : break
        print func(line),

if __name__ == "__main__":
    #filter_stream(lambda line : line)
    #filter_files("data.txt", str.upper)
    filter_stream(str.upper)
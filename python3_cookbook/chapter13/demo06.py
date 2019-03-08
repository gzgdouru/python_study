'''
执行外部命令并获取它的输出
'''
import subprocess

if __name__ == "__main__":
    # out_bytes = subprocess.check_output(['netstat', '-a'])
    # print(out_bytes.decode("gbk"))

    text = b'''
    hello world
    this is a test
    goodbye
    '''

    p = subprocess.Popen(["wc"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = p.communicate(text)

    out = stdout.decode("utf-8")
    # err = stderr.decode("utf-8")
    print(out)
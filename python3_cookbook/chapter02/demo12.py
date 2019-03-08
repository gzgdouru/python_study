'''
审查清理文本字符串
'''

if __name__ == "__main__":
    s = 'pýtĥöñ\fis\tawesome\r\n'
    print(repr(s))
    remap = {
        ord('\t'): ' ',
        ord('\f'): ' ',
        ord('\r'): '',
    }
    a = s.translate(remap)
    print(repr(a))
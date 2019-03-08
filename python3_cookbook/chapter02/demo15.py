'''
字符串中插入变量
'''

if __name__ == "__main__":
    s = '{name} has {n} messages.'
    print(s.format(name="Guido", n=37))

    name = "Guido"
    n = 37
    print(s.format_map(vars()))

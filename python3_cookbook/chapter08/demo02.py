'''
自定义字符串的格式化
'''
_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if format_spec == '':
            format_spec = "ymd"
        fmt = _formats[format_spec]
        return fmt.format(d=self)


if __name__ == "__main__":
    d = Date(2019, 1, 17)
    print(format(d))
    print(format(d, 'dmy'))
    print("this date is {:ymd}".format(d))
    print("this date is {:dmy}".format(d))

'''
将单方法的类转换为函数
'''
from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self._template = template

    def open(self, **kwargs):
        return urlopen(self._template.format_map(kwargs))


def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener


if __name__ == "__main__":
    # yahoo = UrlTemplate("http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}")
    # for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
    #     print(line.decode("utf-8"))

    yahoo = urltemplate("http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}")
    for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
        print(line.decode("utf-8"), end="")

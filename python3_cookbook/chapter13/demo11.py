'''
给简单脚本增加日志功能
'''
import logging

if __name__ == "__main__":
    logging.basicConfig(
        filename="app.log",
        level=logging.ERROR,
        format= "%(levelname)s:%(asctime)s:%(message)s"
    )

    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')

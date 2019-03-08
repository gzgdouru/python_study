'''
读取配置文件
'''
from configparser import ConfigParser

if __name__ == "__main__":
    cfg = ConfigParser()
    cfg.read("config.ini")
    print(cfg.sections())
    print(cfg.get('installation','library'))
    print(cfg.getboolean('debug','log_errors'))
    print(cfg.getint('server', 'port'))
    # print(cfg.get('server', 'signature'))
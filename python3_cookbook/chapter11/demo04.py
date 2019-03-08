import ipaddress

if __name__ == "__main__":
    net = ipaddress.ip_network('123.45.67.64/27')
    print(net)

    for a in net:
        print(a)

    print("-" * 80)
    net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
    print(net6)

    for a in net6:
        print(a)

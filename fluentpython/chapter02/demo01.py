'''
使用列表推导式计算笛卡儿积
'''

if __name__ == "__main__":
    colors = ["black", "white"]
    sizes = ["S", "M", "L"]

    tshirts = [(color, size) for color in colors for size in sizes]
    print(tshirts)
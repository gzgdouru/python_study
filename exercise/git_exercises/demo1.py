# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import uuid

if __name__ == "__main__":
    for i in range(200):
        print(str(uuid.uuid1()))
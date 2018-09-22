#将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中
from mysqlDB import mysqlDB
import uuid

if __name__ == "__main__":
    mysqlDB.connectDB({
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "passwd": "123456",
        "db": "mytest",
        "charset": "utf8",
    })

    for i in range(200):
        id = str(uuid.uuid1())
        sql = "insert into tb_coupon(id) values('{id}')".format(id=id)
        bRes, result = mysqlDB.execute(sql)
        if not bRes:
            print("execute {sql} error!".format(sql=sql))


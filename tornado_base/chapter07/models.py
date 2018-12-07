from datetime import datetime

import peewee
import peewee_async

db = peewee.MySQLDatabase("peewee_test", host="localhost", port=3306, user="root", password="123456", charset="utf8")

async_db = peewee_async.MySQLDatabase("peewee_test", host="localhost", port=3306, user="root", password="123456", charset="utf8")
objects = peewee_async.Manager(async_db)
async_db.set_allow_sync(False)


class Supplier(peewee.Model):
    name = peewee.CharField(max_length=100, verbose_name="名称", index=True)
    address = peewee.CharField(max_length=100, verbose_name="联系地址")
    phone = peewee.CharField(max_length=11, verbose_name="联系电话")

    class Meta:
        table_name = "tb_supplier"
        database = db


class Goods(peewee.Model):
    supplier = peewee.ForeignKeyField(Supplier, verbose_name="供应商", backref="goods")
    name = peewee.CharField(max_length=100, verbose_name="商品名称", index=True)
    click_num = peewee.IntegerField(default=0, verbose_name="点击数")
    goods_num = peewee.IntegerField(default=0, verbose_name="库存数")
    price = peewee.FloatField(default=0.0, verbose_name="价格")
    brief = peewee.TextField(verbose_name="商品简介")

    class Meta:
        table_name = "tb_goods"
        database = db


def init_table():
    db.create_tables([Supplier, Goods])


if __name__ == "__main__":
    init_table()

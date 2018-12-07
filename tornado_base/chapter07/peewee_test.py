import peewee

from models import Supplier, Goods
from data import supplier_list, goods_list


def save_model():
    for supplier in supplier_list:
        supplier_obj = Supplier()
        supplier_obj.name = supplier["name"]
        supplier_obj.address = supplier["address"]
        supplier_obj.phone = supplier["phone"]
        supplier_obj.save()

    for record in goods_list:
        good = Goods(**record)
        good.save()

    pass


def query_model():
    # 获取某一条数据
    # good = Goods.get(Goods.id == 1)
    # good = Goods.get_by_id(1)
    # good = Goods[1]

    # select 返回的是modelselect对象
    # 获取所有数据
    # select price from goods
    goods = Goods.select()

    # select * from goods where price > 100
    goods = Goods.select().where(Goods.price > 100)

    # select * from goods where price>100 and click_num>200
    goods = Goods.select().where((Goods.price > 100) & (Goods.click_num > 200))

    # select * from goods where name like "%飞天"
    goods = Goods.select().where(Goods.name.contains("飞天"))

    # select * from goods where id in (1, 3)
    # goods = Goods.select().where(Goods.id<<[1, 3])
    # goods = Goods.select().where((Goods.id == 1) | (Goods.id == 3))
    goods = Goods.select().where(Goods.id.in_([1, 3]))

    # select * from goods where price>click_num
    goods = Goods.select().where(Goods.price > Goods.click_num)

    # 排序 select * from goods order by price desc
    # goods = Goods.select().order_by(Goods.price)
    goods = Goods.select().order_by(-Goods.price)

    # 分页
    # goods = Goods.select().order_by(Goods.price).paginate(1, 2)

    for good in goods:
        print(good.name, good.price)
    pass


def update_model():
    good = Goods.get_by_id(2)
    #更新
    # good.click_num += 1
    # good.save()
    # Goods.update(click_num=Goods.click_num + 1).where(Goods.id == 1).execute()

    #删除
    # good.delete_instance()
    Goods.delete().where(Goods.id==2).execute()


if __name__ == "__main__":
    # save_model()

    # query_model()

    # update_model()

    good = Goods.select().where(Goods.price>1000).exists()
    print(good)


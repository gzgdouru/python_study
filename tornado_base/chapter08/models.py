import peewee

db = peewee.MySQLDatabase(database="mytest", host="127.0.0.1", port=3306, user="root", password="123456",
                          charset="utf8")


class Message(peewee.Model):
    id = peewee.AutoField(primary_key=True)
    name = peewee.CharField(max_length=64)
    email = peewee.CharField(max_length=64)
    address = peewee.CharField(max_length=255)
    message = peewee.TextField()

    class Meta:
        database = db
        table_name = "tb_message"

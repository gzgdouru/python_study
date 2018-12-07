import os

from tornado import web, ioloop
import aiomysql


class MainHandler(web.RequestHandler):
    def initialize(self, db_config):
        self.db_config = db_config

    async def get(self, *args, **kwargs):
        id = ""
        name = ""
        email = ""
        address = ""
        message = ""
        async with aiomysql.create_pool(**self.db_config) as pool:
            async with pool.get() as conn:
                async with conn.cursor() as cur:
                    await cur.execute("select id, name, email, address, message from tb_message")
                    try:
                        id, name, email, address, message = await cur.fetchone()
                    except Exception as e:
                        pass
        self.render("message.html", id=id, name=name, email=email, address=address, message=message)

    async def post(self, *args, **kwargs):
        id = self.get_argument("id", "")
        name = self.get_argument("name", "")
        email = self.get_argument("email", "")
        address = self.get_argument("address", "")
        message = self.get_argument("message", "")
        async with aiomysql.create_pool(**self.db_config) as pool:
            async with pool.get() as conn:
                async with conn.cursor() as cur:
                    if not id:
                        sql = '''
                        insert into tb_message(name, email, address, message)
                        values('{name}', '{email}', '{address}', '{message}'
                        '''.format(name=name, email=email, address=address, message=message)
                        await cur.execute(sql)
                        await cur.execute("select id, name, email, address, message from tb_message")
                        id, name, email, address, message = await cur.fetchone()
                    else:
                        sql = '''
                        update tb_message set name='{name}', email='{email}', address='{address}', message='{message}'
                        where id={id}
                        '''.format(name=name, email=email, address=address, message=message, id=id)
                        print(sql)
                        await cur.execute(sql)
        self.render("message.html", id=id, email=email, name=name, address=address, message=message)


settings = {
    "static_path": os.path.join(os.path.abspath(os.path.dirname(__file__)), "static"),
    "static_url_prefix": "/static/",
    "template_path": "templates",
}

if __name__ == "__main__":
    db_config = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "db": "mytest",
        "charset": "utf8",
        "autocommit": True,
    }

    app = web.Application([
        web.URLSpec(r'/', MainHandler, {"db_config": db_config}, name="index"),
    ], debug=True, **settings)
    app.listen(8888)
    ioloop.IOLoop.current().start()

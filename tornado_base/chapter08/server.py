import os
import aiomysql

from tornado import web, ioloop

from chapter08.forms import MessageForm
from chapter08.models import Message


class MainHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        message_form = MessageForm()
        self.render("message.html", message_form=message_form)

    async def post(self, *args, **kwargs):
        message_form = MessageForm(self.request.arguments)
        if message_form.validate():
            name = message_form.name.data
            email = message_form.email.data
            address = message_form.address.data
            msg = message_form.message

            message = Message()
            message.name = name
            message.email = email
            message.address = address
            message.message = msg
            message.save()
        self.render("message.html", message_form=message_form)


settings = {
    "static_path": os.path.join(os.path.abspath(os.path.dirname(__file__)), "static"),
    "static_url_prefix": "/static/",
    "template_path": "templates",
}

if __name__ == "__main__":
    app = web.Application([
        web.URLSpec(r'/', MainHandler, name="index"),
    ], debug=True, **settings)
    app.listen(8888)
    ioloop.IOLoop.current().start()

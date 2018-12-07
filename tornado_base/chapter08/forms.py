from wtforms.fields import StringField, TextAreaField
from wtforms_tornado import Form
from wtforms.validators import DataRequired, Length, Email


class MessageForm(Form):
    name = StringField("姓名", validators=[DataRequired(message="请输入姓名")])
    email = StringField("邮件", validators=[Email("邮箱不合法")])
    address = StringField("地址", validators=[DataRequired(message="请填写地址")])
    message = TextAreaField("留言", validators=[DataRequired(message="请填写留言")])

if __name__ == "__main__":
    pass

import numbers


class Filed:
    pass


class IntegerField(Filed):
    def __init__(self, db_column="", min_value=None, max_value=None):
        self._value = None
        self.db_column = db_column
        self.min_value = min_value
        self.max_value = max_value

        if not isinstance(self.min_value, numbers.Integral):
            raise ValueError("min_value must be int")

        if not isinstance(self.max_value, numbers.Integral):
            raise ValueError("max_value must be int")

        if self.min_value and self.max_value and (self.min_value > self.max_value):
            raise ValueError("min_value must be smaller than max_value")

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        elif value < self.min_value or value > self.max_value:
            raise ValueError("value must between min_value and max_value")
        else:
            self._value = value


class CharField(Filed):
    def __init__(self, db_column="", max_length=None):
        self._value = None
        self.db_column = db_column
        self.max_length = max_length

        if not self.max_length:
            raise ValueError("you must spcify max_lenth for charfiled")

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("string value need")
        elif len(value) > self.max_length:
            raise ValueError("value len excess len of max_length")
        else:
            self._value = value


class ModelMetaClass(type):
    def __new__(cls, class_name, class_parent, class_attr, **kwargs):
        if class_name == "BaseModel":
            return super().__new__(cls, class_name, class_parent, class_attr, **kwargs)

        # 提取字段
        field_attr = {}
        for key, value in class_attr.items():
            if isinstance(value, Filed):
                field_attr[key] = value
        class_attr["fields"] = field_attr

        # 提取表名
        db_table = class_name.lower()
        meta_attr = class_attr.get("Meta")
        if meta_attr and getattr(meta_attr, "db_table", None):
            db_table = getattr(meta_attr, "db_table", None)
            del class_attr["Meta"]
        _meta = {"db_table": db_table}
        class_attr["_meta"] = _meta

        return super().__new__(cls, class_name, class_parent, class_attr, **kwargs)


class BaseModel(metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):
        for field_name, field_value in kwargs.items():
            setattr(self, field_name, field_value)
        return super().__init__()

    def save(self):
        fields = []
        values = []
        for field_key, field_value in self.fields.items():
            db_column = field_value.db_column
            if not db_column:
                db_column = field_key.lower()
            fields.append(db_column)
            value = getattr(self, field_key)
            if isinstance(value, str):
                values.append("'{0}'".format(value))
            else:
                values.append(str(value))
        db_table = self._meta["db_table"]
        sql = "insert into {table}({fields}) values({values})".format(table=db_table, fields=",".join(fields),
                                                                      values=",".join(values))
        print(sql)


class Student(BaseModel):
    name = CharField(max_length=32)
    age = IntegerField(min_value=0, max_value=150)

    class Meta:
        db_table = "tb_student"


if __name__ == "__main__":
    student = Student(name="ouru", age=26)
    student.save()

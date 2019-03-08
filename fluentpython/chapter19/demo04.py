'''
使用shelve模块调整oscon数据源的结构
'''
import warnings
import shelve

from chapter19.demo01 import load

DB_NAME = "schedule_db"
CONFERENCE = "conference.115"


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def load_db(db):
    raw_data = load()
    warnings.warn("loading " + DB_NAME)
    for collection, rec_list in raw_data["Schedule"].items():
        record_type = collection[:-1]
        for record in rec_list:
            key = "{}.{}".format(record_type, record["serial"])
            record["serial"] = key
            db[key] = Record(**record)


if __name__ == "__main__":
    with shelve.open(DB_NAME) as db:
        if CONFERENCE not in db:
            load_db(db)

        speaker = db["event.33451"]
        print(speaker)

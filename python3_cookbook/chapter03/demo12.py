'''
基本的日期与时间转换
'''
from datetime import datetime, timedelta

if __name__ == "__main__":
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print(c.days)
    print(c.seconds / 3600)
    print(c.total_seconds() / 3600)

    a = datetime(2012, 9, 23)
    print(a + timedelta(days=10))
    b = datetime(2012, 12, 21)
    d = b - a
    print(d.days)

    now = datetime.today()
    print(now)
    print(now + timedelta(minutes=10))

    a = datetime(2012, 3, 1)
    b = datetime(2012, 2, 28)
    print((a - b).days)
    a = datetime(2013, 3, 1)
    b = datetime(2013, 2, 28)
    print((a - b).days)

    from dateutil.relativedelta import relativedelta

    a = datetime(2012, 9, 23)
    print(a + relativedelta(months=+1))
    print(a + relativedelta(months=+4))

    b = datetime(2012, 12, 21)
    d = b - a
    print(d)

    d = relativedelta(b, datetime(2012, 12, 22))
    print(d)

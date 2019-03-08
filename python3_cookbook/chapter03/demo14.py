# -*- coding: utf-8 -*-
'''
计算当前月份的日期范围
'''
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
import calendar


def get_month_range(start_date=None):
    if not start_date:
        start_date = datetime.now().replace(day=1)
    weeks_in_month, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)


def date_range(start, stop, sep):
    while start < stop:
        yield start
        start += sep


def date_range_2(start, stop, sep):
    date_list = []
    while start < stop:
        date_list.append(start)
        start += sep
    return date_list


if __name__ == "__main__":
    a_day = timedelta(days=1)
    first_day, last_day = get_month_range(datetime.now())

    # for d in date_range(first_day, last_day, timedelta(days=1)):
    # for d in date_range(datetime.now(), datetime.now() + relativedelta(months=+1), timedelta(days=1)):
    #     print(d.strftime("%Y/%m/%d"))

    # while first_day < last_day:
    #     print(first_day)
    #     first_day += a_day
    for d in date_range(datetime.now(), datetime.now() + relativedelta(months=+1), timedelta(days=1)):
        print(d.strftime("%Y/%m/%d"))

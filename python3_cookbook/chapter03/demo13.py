'''
计算最后一个周五的日期
'''
from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if not start_date:
        start_date = datetime.now()
        day_num = start_date.weekday()
        day_num_target = weekdays.index(dayname)
        days_ago = (7 + day_num - day_num_target) % 7
        if days_ago == 0:
            days_ago = 7
        target_date = start_date - timedelta(days=days_ago)
        return target_date


if __name__ == "__main__":
    print(get_previous_byday("Thursday"))

    from dateutil.relativedelta import relativedelta
    from dateutil import rrule

    d = datetime.now()
    print(d + relativedelta(weekday=rrule.TH))
    print(d + relativedelta(weekday=rrule.TH(-1)))

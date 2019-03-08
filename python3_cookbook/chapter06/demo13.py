'''
数据的累加与统计操作
'''
import pandas

from custom import cprint

if __name__ == "__main__":
    rats = pandas.read_csv("data.csv")
    cprint(rats)

    cprint(rats["Date"].unique())

    crew_dispatched = rats[rats["Date"] == "6/11/2007"]
    cprint(len(crew_dispatched))

    cprint(crew_dispatched["Symbol"].value_counts())

    dates = crew_dispatched.groupby('Volume')
    cprint(len(dates))

    date_counts = dates.size()
    cprint(date_counts)

import datetime


def test():
    # datetime.date represents standard date;
    # datetime.time represents standard time, independent from the date;
    # datetime.timedelta represents the difference between two points in time;
    # datetime.tzinfo represents timezones;
    # datetime.datetime represents both time and date together.
    vostok_1 = datetime.datetime(1961, 4, 12, 6, 7)
    print(vostok_1)  # 1961-04-12 06:07:00
    print(vostok_1.time())  # 06:07:00
    print(vostok_1.date())  # 1961-04-12

    print(datetime.datetime.now())
    print(datetime.datetime.today())


def test_two():
    current_datetime = datetime.datetime(2021, 8, 20, 21, 40, 15)
    return current_datetime


def format_parse():
    # %d	Day of the month — 01, 02, ..., 31
    # %m	Month as a number — 01, 02, ..., 12
    # %y	Year without century — 00, 01, ..., 99
    # %Y	Year with century — 0001, ..., 2020, ..., 9999
    # %H	Hour (24 hours) — 00, 01, ..., 23
    # %I	Hour (12 hours) — 01, 02, ..., 12
    # %M	Minutes — 00, 01, ..., 59
    # %S	Seconds — 00, 01, ..., 59
    # %B	Month as the area's full name — January, February, ..., December

    date_string = "06/04/2020 12:30"
    dt1 = datetime.datetime.strptime(date_string, "%m/%d/%Y %H:%M")
    print(dt1)  # 2020-06-04 12:30:00
    dt2 = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
    print(dt2)  # 2020-04-06 12:30:00
    dt3 = datetime.datetime.strptime(date_string, "%d/%m/%Y %I:%M")
    print(dt3)  # 2020-04-06 00:30:00

    dt4 = datetime.datetime(2020, 6, 4, 12, 30)
    date_string1 = dt4.strftime("%B %d, %Y at %H:%M")
    print(date_string1)  # June 04, 2020 at 12:30
    date_string2 = dt4.strftime("%d.%m.%y")
    print(date_string2)  # 04.06.20
    date_string3 = dt4.strftime("%Y-%m-%d-%I:%M")
    print(date_string3)  # 2020-06-04-12:30
    date_string4 = dt4.strftime("The event will take place on %B %d.")
    print(date_string4)  # The event will take place on June 04.


def day_of_the_week(date):
    dt1 = datetime.datetime.strptime(date, "%Y-%m-%d")
    print(dt1.strftime("%A"))


if __name__ == '__main__':
    # test()
    # print(test_two())
    # format_parse()
    day_of_the_week('2014-11-08')
    day_of_the_week('2019-12-31')


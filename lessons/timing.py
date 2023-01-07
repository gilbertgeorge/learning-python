import time


def timing():
    current_time = time.gmtime()
    action = "to feed the cat"

    # raw time object
    # print(f"It's {current_time}. Time {action}.")

    # formatted time object
    current_time = time.asctime(time.gmtime())
    print(f"It's {current_time}. Time {action}.")

    # formatted time object (directives)
    current_time = time.strftime("%H:%M", time.gmtime())
    print(f"It's {current_time}. Time {action}.")

    # local time object (formatted with directives)
    current_time = time.strftime("%H:%M", time.localtime())
    print(f"It's {current_time}. Time {action}.")


def measurement():
    action2 = "to feed the dog"
    time.sleep(3)
    current_time = time.strftime("%H:%M", time.localtime())
    print(f"It's {current_time}. Time {action2}.")


def epoch():
    print(time.time())
    print(time.asctime())
    print(time.ctime(time.time()))
    print(time.gmtime(0))


def difference():
    action = "to feed the snail"
    last_time = time.time()
    current_time = time.strftime("%H:%M", time.localtime())
    print(f"It's {current_time}. Time {action}.")

    time.sleep(3)
    new_cur_time = time.time()
    time_passed = float((new_cur_time - last_time) / 60)
    print(f"You have fed the cat {time_passed} minutes ago.")


def difference_perf():
    start = time.perf_counter()
    print("Oh no! The cat's breaking his diet!")
    end = time.perf_counter()
    total_time = end - start
    print(f"Your program has executed for {total_time} seconds.")


def zoning():
    print(time.timezone / 3600)
    print(time.tzname)
    print(time.timezone)
    print(time.daylight)


if __name__ == '__main__':
    # timing()
    # measurement()
    epoch()

    # difference()
    # difference_perf()

    zoning()

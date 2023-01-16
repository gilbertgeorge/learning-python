import time
import _thread
from threading import Thread, Lock, Semaphore


def greet(lock_object):
    time.sleep(3)
    print('Hello, ')
    # Release the lock as we are done here
    lock_object.release()


def create_thread(locks):
    # Create a lock and acquire it
    lock_object = _thread.allocate_lock()
    lock_object.acquire()

    # Store it in the global lock list
    locks.append(lock_object)
    # Pass it to a new thread that can release the lock once done
    _thread.start_new_thread(greet, (lock_object,))


def use__thread():
    locks = []
    create_thread(locks)
    print('world!')
    # Acquire all locks = release all threads
    all(lock.acquire() for lock in locks)


def greetings():
    time.sleep(3)
    print('Hello, ')


def use_threading():
    t = Thread(target=greetings)
    t.start()
    print('world!')


def cube_area(thread, length, delay=0):
    time.sleep(delay)
    print(f"{thread} ---> Area of a cube with an edge length of {length} is: \t{6 * (length ** 2)}")


def circle_area(thread, length, delay=0):
    time.sleep(delay)
    print(f"{thread} ---> Area of a circle with a radius length of {length} is: \t{3.14 * (length ** 2)}")


def threading_example_one():
    t1 = Thread(target=cube_area, args=("t1", 2))
    t2 = Thread(target=circle_area, args=("t2", 3))

    t3 = Thread(target=cube_area, args=("t3", 4))
    t4 = Thread(target=circle_area, args=("t4", 6))

    t5 = Thread(target=cube_area, args=("t5", 9))
    t6 = Thread(target=circle_area, args=("t6", 8))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()


def threading_example_two():
    t1 = Thread(target=cube_area, args=("t1", 2, 3))
    t2 = Thread(target=circle_area, args=("t2", 2, 2))

    t3 = Thread(target=cube_area, args=("t3", 4, 1))
    t4 = Thread(target=circle_area, args=("t4", 6, 2))

    t5 = Thread(target=cube_area, args=("t5", 9, 4))
    t6 = Thread(target=circle_area, args=("t6", 8, 3))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()


def num():
    for i in range(1, 6):
        print("The number is: ", i)
        time.sleep(1)


def double_num():
    for i in range(1, 6):
        print("The double of the number is: ", i * 2)
        time.sleep(1)


def square_num():
    for i in range(1, 6):
        print("The square of the number is: ", i ** 2)
        time.sleep(1)


def lets_count():
    thread_1 = Thread(target=num)
    thread_2 = Thread(target=double_num)
    thread_3 = Thread(target=square_num)

    thread_1.start()
    time.sleep(0.2)
    thread_2.start()
    time.sleep(0.2)
    thread_3.start()


l = Lock()
total = 0
sem = Semaphore(3)


def calc_price(name, item_price):
    for i in range(3):
        l.acquire()
        print("Item:", name)
        time.sleep(2)
        total = item_price
        print("Price:", total)
        l.release()


def lock_race():
    t1 = Thread(target=calc_price, args=("Shirt", 5))
    t2 = Thread(target=calc_price, args=("Jeans", 10))

    t1.start()
    t2.start()


def new_calc_price(name, item_price):
    with sem:
        for i in range(2):
            print("Item:", name)
            time.sleep(10)
            total = item_price
            print("Price:", total)


def semaphore_race():
    # creating multiple threads
    t1 = Thread(target=new_calc_price, args=("Shirt", 5))
    t2 = Thread(target=new_calc_price, args=("Jeans", 10))
    t3 = Thread(target=new_calc_price, args=("Dress", 12))
    t4 = Thread(target=new_calc_price, args=("Belt", 3))
    t5 = Thread(target=new_calc_price, args=("Bag", 20))

    # calling the threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()


if __name__ == '__main__':
    # use__thread()
    # use_threading()
    # threading_example_one()
    # threading_example_two()
    # lets_count()

    # lock_race()
    semaphore_race()

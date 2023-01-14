import time
import _thread
from threading import Thread


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


if __name__ == '__main__':
    # use__thread()
    # use_threading()
    # threading_example_one()
    threading_example_two()

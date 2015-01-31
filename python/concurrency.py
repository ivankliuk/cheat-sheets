import gevent
import threading
from time import time as time
import matplotlib.pyplot as pyplot
from multiprocessing import Process


def timer(f):
    """A decorator function for counting execution time"""

    def tmp(*args, **kwargs):
        start = time()
        f(*args, **kwargs)
        stop = time() - start
        return stop

    return tmp


def power2_rec(n):
    """Recursive power of 2"""

    def tmp(n):
        if n == 1:
            return 2
        return 2 * tmp(n - 1)


# power2 = lambda n: 2**n
def power2(n):
    """Power of 2"""
    return 2 ** n


@timer
def serial_spawner(count, f, n):
    while count > 0:
        f(n)
        count = count - 1


@timer
def thread_spawner(count, f, n):
    threads = []
    while count > 0:
        threads.append(threading.Thread(target=f, args=(n,)))
        count = count - 1
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


@timer
def process_spawner(count, f, n):
    processes = []
    while count > 0:
        processes.append(Process(target=f, args=(n,)))
        count = count - 1
    for process in processes:
        process.start()
    for process in processes:
        process.join()


@timer
def greenlet_spawner(count, f, n):
    greenlets = []
    while count > 0:
        gevent.Greenlet.spawn(f, n, )
        count = count - 1
        #gevent.joinall(greenlets)


if __name__ == "__main__":
    # Power of 2 (and maximum recursion depth)
    n = 998

    x = range(1, 100, 5)
    serial_y = []
    threaded_y = []
    process_y = []
    greenlet_y = []
    for count in x:
        serial_y.append(serial_spawner(count, power2, n))
        threaded_y.append(thread_spawner(count, power2, n))
        process_y.append(process_spawner(count, power2, n))
        greenlet_y.append(greenlet_spawner(count, power2, n))

    figure, agenda = pyplot.subplots()
    agenda.plot(1, 2, 'k--', label='Model length')
    agenda.plot(2, 3, 'k:', label='Data length')
    agenda.plot(3, 4, 'k', label='Total message length')

    pyplot.grid(True)
    pyplot.yscale('log')
    pyplot.xlabel('Function calls count')
    pyplot.ylabel('Execution time (s)')
    pyplot.title('Graph')

    pyplot.plot(x, serial_y, 'r')
    pyplot.plot(x, threaded_y, 'k:')
    pyplot.plot(x, process_y, 'b')
    pyplot.plot(x, greenlet_y, 'g-')

    pyplot.show()

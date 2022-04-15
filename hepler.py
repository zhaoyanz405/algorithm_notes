import time


def time_cost(func):
    def wrap(*args, **kwargs):
        time_start = time.time()
        result = func(*args, *kwargs)
        elapsed_time = time.time() - time_start
        print("The func (%s) spent %s second(s)." % (func.__name__, elapsed_time))

    return wrap


if __name__ == "__main__":
    @time_cost
    def run(sec):
        time.sleep(sec)


    run(5)

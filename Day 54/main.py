import time

def speed_calc_decorator(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"{func.__name__} run speed: {end_time - start_time}s")
        return result

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
         i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()
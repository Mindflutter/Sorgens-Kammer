import time


# Outermost layer 1 - for dec to be able to accept arguments
def dec_with_arg(log_level):
    """ Decorator that accepts an argument and prints arguments of the decorated function """
    # Layer 2 - for dec to take a function as an argument
    def actual_dec(func):
        # Innermost layer 3 - the thing doing all the job
        def wrapped(*args, **kwargs):
            print(log_level, args, kwargs)
            func(*args, **kwargs)

        return wrapped

    return actual_dec


@dec_with_arg('DEBUG')
def func_with_any_args(*args, **kwargs):
    pass


def usual_dec(func):
    """ Decorator measuring func execution time. """
    def wrapped():
        start = time.time()
        func()
        finish = time.time() - start
        print(f"Function {func.__name__} took {finish:.3f} seconds")

    return wrapped


@usual_dec
def some_func(sleep_time=1):
    time.sleep(sleep_time)


some_func()

# This will print: DEBUG (1, 12) {'k': 'asdasd', 'b': 3}
func_with_any_args(1, 12, b=3, k='asdasd')

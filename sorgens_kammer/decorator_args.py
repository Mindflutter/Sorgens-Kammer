""" Decorator that accepts an argument and prints arguments of the decorated function """


# Outermost layer 1 - for dec to be able to accept arguments
def dec_with_arg(log_level):
    # Layer 2 - for dec to take a function as an argument
    def actual_dec(func):
        # Innermost layer 3 - the thing doing all the job
        def wrapped(*args, **kwargs):
            print log_level, args, kwargs
            func(*args, **kwargs)
        return wrapped
    return actual_dec


@dec_with_arg('DEBUG')
def func_with_any_args(*args, **kwargs):
    pass


# This will print: DEBUG (1, 12) {'k': 'asdasd', 'b': 3}
func_with_any_args(1, 12, b=3, k='asdasd')

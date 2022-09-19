def loop_list(the_list: list):
    """ Return a generator that will infinitely iterate the given list. """
    list_size = len(the_list)
    num = 0
    while num < list_size:
        yield the_list[num]
        num += 1
        if num >= list_size:
            num = 0

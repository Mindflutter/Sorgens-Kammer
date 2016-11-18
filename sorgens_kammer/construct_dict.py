from itertools import izip, izip_longest


def construct_dict(key_list, value_list):
    """ Constructs a dict out of two lists of keys and values.
    Sets excessive keys to None, ignores excessive values.
    """
    # TODO: param validation (have to be lists)
    # keys must be unique
    key_list = list(set(key_list))
    if len(key_list) > len(value_list):
        return dict(izip_longest(key_list, value_list))
    else:
        return dict(izip(key_list, value_list))


k = [1, 1, 1, 2, 3, 4, 1, 1, 5, 5, 2, 1, 6]
v = ['', 2, 3, 4, 5, 6]

print construct_dict(k, v)

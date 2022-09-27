# arguments are passed by reference. list contents will be modified
# don"t actually use lists as default args
def f(the_list=[]):
    print(id(the_list))
    the_list.append(1)
    return the_list


# same thing with dicts: gets updated
def dict_gotcha(d: dict):
    d.update({"added": "data"})


the_dict = {"some": "data"}
dict_gotcha(the_dict)
print(the_dict)

# same id, same l
print(f())
print(f())
print(f())

# different id, l redefined
print(f(the_list=[2]))
print(f(the_list=[3, 4]))

# previous l again!
print(f())
print(f())

# note different ids, coz strings are immutable
s = "fizz"
print(id(s))
s += "buzz"
print(id(s))
print(s)

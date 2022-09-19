# arguments are passed by reference. list contents will be modified
def f(l=[]):
    print(id(l))
    l.append(1)
    return l


# same id, same l
print(f())
print(f())
print(f())

# different id, l redefined
print(f(l=[2]))
print(f(l=[3, 4]))

# previous l again!
print(f())
print(f())

# note different ids, coz strings are immutable
s = 'fizz'
print(id(s))
s += 'buzz'
print(id(s))
print(s)

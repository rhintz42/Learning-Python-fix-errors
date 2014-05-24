def bar(l):
    l.append("Hello')
    return l

def foo():
    return bar([])

print("Should print out a list with 'Hello' in it")
print(foo())

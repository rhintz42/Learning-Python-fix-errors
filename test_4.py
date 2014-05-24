def foo():
    a = []
    a.append("Hello")
    return a[len(a)]

print("This should print out the last element in the list `a`")
print(foo())

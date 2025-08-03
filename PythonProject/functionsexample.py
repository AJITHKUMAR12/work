def func():
    x=10
    def func2(x):
        return x+1
    return func2(x+2)
print(func())


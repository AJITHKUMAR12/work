def welcome():
    print("Welcome to Python Programming")
welcome()

def add(x,y):
    print(x+y)
add(1,2)

def add(x=0,y=0):
    print(x+y)
x=int(input("enter a number"))
y=int(input("enter a number"))
add(x,y)

def add(*a):
    total = 0
    for x in a:
        total=total+x
    print(total)
add(1,2,3,56,56)


def listing(lst):
    lst[2]=0
    print(lst)
listing([1,2,3,56,56])


def sum(a,b):
    return a+b
result=sum(1,2)
print(result)

a=20
if a>8:
    print("a is greater than 8")
    if a>21:
        print("a is greater than 21")
    else:
        print("a is not greater than 21")
else:
    print("a is not greater than 8")


a=12
if a%3==0:
    print("a is divisble by 3")
elif a%2==0:
    print("a is divisble by 2")
else:
    print("a is not divisble by 2 and 3")



var=int(input("enter a number"))
while var%7!=0:
    var=int(input("enter a number"))
print("%d it is multiple of 7"%var)


var1=[1,2,3,4,5,6,67,7]
for i in var1:
    print(i)

x="this is the ak. ajith kymar"
for i in x:
    if(i=="."):
        break;
    print(i,end="")

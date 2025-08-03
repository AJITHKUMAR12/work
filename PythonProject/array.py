from array import *
arr=array('i',[1,2,3,4,5])
print(arr)
print(arr[4])
for i in arr:
    print(i)
for pnt in range(1,len(arr)-1):
    print(pnt,arr[pnt])
arr.reverse()
print(arr)
arr.append(89)
print(arr)
arr.remove(3)
print(arr)
print(arr.index(89))


arr1= array('i',[])
x=int(input("enter a number"))
print("enter %d elements"%x)
for i in range(x):
    n=int(input("enter a number"))
    arr1.append(n)
print(arr1)
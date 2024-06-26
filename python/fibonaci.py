a=0
b=1
num=int(input("enter num "))
if num==1:
    print(b)
else:
    for i in range(0,num+1):
        c=a+b
        a=b
        b=c
        print(b)

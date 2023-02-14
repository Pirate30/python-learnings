# iterating 2+ lists at the same time
a=[1,2,3,4,5,6]
b=[10,20,30,40,50,60,70]
c=[100,200,300,400,500,600,700,800]

for x,y,z in zip(a,b,c):
    print(x,y,z)
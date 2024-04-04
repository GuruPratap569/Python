#do this in python shell for better response

List = [1,2,3,4]
I = iter(List)
print(I)
#item = I.__next__() --or--
item = next(I)
print(item)           #print 1
item = next(I)
print(item)           #print 2
item = next(I)
print(item)            #print 3

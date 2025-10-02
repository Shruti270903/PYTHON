l1= [1,2,3,4,5]
l1.reverse()  #for reverse any list
print(l1)
l1_copy = l1.copy()    #for copy any list
print(l1_copy)   
print(id(l1_copy), id(l1)) #for printing address of list
l1.sort()   #for sorting list
print(l1)
print(l1_copy)
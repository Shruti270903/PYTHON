
first = [11,14,21,32,81,12]
first.append(22)  #add element in end of the list
print(first)
first.remove(14)  # remove element which we give
print(first)
first.pop()  # remove element from end of the list
print(first)
first.pop(3)  #remove 3 index element from the list
print(first)
first.insert(3,33)  #insert element 33 in place of index 3 
print(first)
idx = first.index(32)
print(idx)
first.sort()  #sort will arrange hole lit in increasing order
print(first)

# built-in function in list
print(len(first) ) 
print(max(first))
print(min(first))
print(sum(first))
del(first)

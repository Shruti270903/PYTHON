fruits= ('apple', 'mango', 'strawberry', 'grapes', 'bnana', 'apple', 'mango')
print(fruits.count('jackfruit'))
print(fruits.index('mango'))
print(len(fruits))
fruit = ('apple', 'mango', 'bnana', 'mango', 'apple', 'strawberry')
print(fruit[3])  #it will not add jackfruit in tuple fruit
print(fruit[-3])
fruit[3] ='jackfruit'
print(fruit)
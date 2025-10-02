class Student:
    def __init(self, name, marks):
        self.name= name
        self.marks= marks
    def get__avg(self):
        sum = 0
for val in self.marks:
    sum += val
print("hi", self.name, "your avg score is :", sum/3 )

s1=Student("tony", [99, 98,97])
s1.get__avg()
s1.name= "ironman"
s1.get_avg()
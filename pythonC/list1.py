# import math
# def sphere_area(radius):
#     return 4*math.pi*radius**2
# def sphere_volume(radius):
#     return (4/3) * math.pi*radius**3
# radius = float(input("Enter the radius of the sphere: "))
# area = sphere_area(radius)
# volume = sphere_volume(radius)
# print("the area of sphere is ", area)
# print("the volume of sphere is : ", volume)

# def detect_number_type(num):
#     if num==0:
#         return "the number is zero."
#     elif num%2 ==0:
#         return "the number is even"
#     else :
#         return "the number is odd"
# number = int(input("Enter  a number : "))
# result = detect_number_type(number)
# print(result)

def classify_temperature(temp):
    if temp>=30:
        return "it,s hot today"
    elif 20<= temp< 30:
        return "it's warm today"
    elif 10<= temp<20:
        return "it's cool today"
    else :
     return "it's cold today"
temperature = float(input("enter the temperature in degres: "))
result = classify_temperature(temperature)
print(result)  

#Day 2: 30 Days of python programming
first_name = "Helios"

import math

last_name = "Suna"
full_name = first_name+last_name
city = 'Indore'
country = "India"
age = 100
year = 2026
is_married  = 'Single'
is_true = True
is_light_on = True
gs, mlbb = 'Sun','Helios'


print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(city))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(gs))
print(type(mlbb))

print(len(first_name))
print(first_name == last_name)

num_one = 5
num_two = 4

print(num_one+num_two)
print(num_one-num_two)
print(num_one*num_two)
print(num_one/num_two)
print(num_one%num_two)
print(num_one//num_two)
print(num_one**num_two)

radius = int(input("Enter radius of circle : "))
area_of_circle = math.pi*radius*radius
circum_of_circle = 2*math.pi*radius
print(round(area_of_circle, 2))
print(round(circum_of_circle, 2))

help('keywords')
help("not")

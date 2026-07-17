import math
def two_num_sum(num1,num2):
    return num1+num2

def area_of_circle(radius):
    return round(math.pi*radius*radius,2)

def sum_of_n_Numbers(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

def convert_celsius_to_fahrenheit(celsius):
    f = (celsius * 9/5) + 32
    return f

def check_season(season):
    Autumn = ['September', 'October', 'November']
    Winter = ['December', 'January', 'February']
    Spring  = ['March', 'April', 'May']
    Summer = ['June', 'July', 'August']

    season = season.capitalize()
    if season in Autumn:
        return "Autumn"
    elif season in Winter:
        return "Winter"
    elif season in Spring:
        return "Spring"
    elif season in Summer:
        return "Summer"
    else:
        return "Enter Valid Month name"

def calculate_slope(x1,x2,y1,y2):
    return (y2-y1)/(x2-x1)

def print_list(lst):
    for i in lst:
        print(i)

def add_item(lst,item):
    lst.append(item)


lst = [2,6,3,11]
add_item(lst,100)
print(lst)
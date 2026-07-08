# age = 100
# height = 175
# comp = 1 + 2j

# base = int(input("Enter Base of Triangle: "))
# heightt = int(input("Enter height of Triangle "))
# print("The area of Triangle is : ",(0.5)*base*heightt)

# a = int(input("Enter a number : "))
# b = int(input("Enter a number : "))
# c = int(input("Enter a number : "))
# print("The perimeter of the triangel is ", a+b+c)

print(('on' in 'python') and ('on' in 'dragon'))

length = len('python')
len_f = float(length)
len_s = str(len_f)

print(length," ",len_f," ",len_s)
print(type(len_s))

#even or not 
num = 69
if(num%2==0):
    print('even')
else :
    print("odd")

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

temp1 = int(2.7)
temp2 = 7//3

print(temp1==temp2)

int_num = '9.8'
str_num = 10

print(int_num==str_num)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years you have lived: "))
seconds = years*365*24*60*60
print(f"You have lived for {seconds} seconds.")
# main.py file
# import mymodule
# print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh

import random
import string

#print(random.randint(100000,999999))



def user_id_gen_by_user(num1,len_id):
    for i in range(num1):
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=len_id))
        print(username)

def rgb_color_gen(num1):
    for i in range(num1):
        parts = []
        for _ in range(3):
            value = random.randint(0, 255)  
            parts.append(str(value))        
        rgb = ','.join(parts)               
        print('rgb('+rgb+')')

def hexa(num1):
    for i in range(num1):
        username = ''.join(random.choices('1234567890abcdef',k=6))
        print('#'+username)

def generate_colors(which,num):
    if which == 'hexa':
        hexa(num)
    else:
        rgb_color_gen(num)


generate_colors('hexa',2)

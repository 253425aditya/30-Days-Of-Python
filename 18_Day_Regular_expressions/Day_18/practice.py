import re
# paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# new_para = re.findall('\w+',paragraph)

# split_para = {}

# for word in new_para:
#     if word in split_para:
#         split_para[word] = split_para[word] + 1
#     else:
#         split_para[word] = 1 

# max_word = max(split_para, key=split_para.get)
# print(f"The most frequent word is '{max_word}' with {split_para[max_word]} occurrences.")

# para = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'

# matches = re.findall('-?\d+',para)
# new = [int(i) for i in matches]
# matches.sort()
# print(new)

# LEVEL-2

# def is_valid_variable(name):
#     pattern = r'^[a-zA-Z][a-zA-Z0-9_]*$'
#     if re.match(pattern,name):
#         return True
#     else:
#         return False

# print(is_valid_variable('first_nam9e'))



# level - 3
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''


cleaned_text = re.sub(r'[%@&$#;]','',sentence)
print(cleaned_text)

new_para = re.findall('\w+',cleaned_text)

split_para = {}

for word in new_para:
    if word in split_para:
        split_para[word] = split_para[word] + 1
    else:
        split_para[word] = 1 

max_word = max(split_para, key=split_para.get)
print(f"The most frequent word is '{max_word}' with {split_para[max_word]} occurrences.")

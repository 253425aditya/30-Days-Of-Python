import os
import json
import re

# with open(r"C:\Users\Hp\Downloads\michelle_obama_speech.txt") as f:
#     text = f.read()

# num_lines = len(text.splitlines())
# num_words = len(text.split())

# print("Lines:", num_lines)
# print("Words:", num_words)

# def most_spoken_lang_list(data,num):
#     lang = {}
#     for i in data:
#         for l in i['languages']:
#             if l in lang:
#                 lang[l] += 1
#             else:
#                 lang[l] = 1

#     sorted_words = dict(
#     sorted(lang.items(), key=lambda item: item[1], reverse=True)[:num]
#     )
#     return sorted_words

# with open(r"C:\Users\Hp\Downloads\countries_data.json", encoding="utf-8") as f:
#     text = f.read()

# data = json.loads(text)

# print(most_spoken_lang_list(data,10))

# def most_populated_countries(data,num):
#     pop = {}
#     for i in data:
#         pop[i['name']] = i['population']

#     sorted_pop = dict(
#     sorted(pop.items(), key=lambda item: item[1], reverse=True)[:num]
#     )
#     return sorted_pop


# print(most_populated_countries(data,10))

'''Level 2'''

with open(r"C:\Users\Hp\Downloads\email_exchanges_big.txt", encoding='utf-8') as f:
    text = f.read()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# print(emails)

print("Total emails:", len(emails))
unique_emails = list(set(emails))

# print(unique_emails)
print("Unique emails:", len(unique_emails))
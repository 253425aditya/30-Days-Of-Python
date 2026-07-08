#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
listt = ['Thirty', 'Days', 'Of', 'Python']
res = ' '.join(listt)
print(res)

company = 'Coding For All'
print(company)
print(len(company))

print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

sliced_list = company.split(' ')
print(sliced_list)

company = company.replace('Coding','Python')
company = company.replace('All','Everyone')

print(company)

fang = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies = fang.split(",")
print(companies)

print(company[0])
print(company[-1])
print(company[10])
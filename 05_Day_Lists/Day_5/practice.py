lst = []
fruits = ['banana', 'orange', 'mango', 'lemon','apple']
leng = len(fruits)

print(fruits[0],fruits[leng//2],fruits[leng-1])

mixed_data_types = ['Aditya',100,176,'Single']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)
print(len(it_companies))
print(it_companies[0],it_companies[leng//2],it_companies[leng-1])
it_companies[0] = 'Baka pvt ltd.'
print(it_companies)
it_companies.append('Facebook')
print(it_companies)
it_companies[0] = it_companies[0].upper()
print(it_companies)
join_it = '#'.join(it_companies)
print(join_it)
print('facebook' in it_companies)
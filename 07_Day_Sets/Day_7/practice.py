# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

length = len(it_companies)
it_companies.add('Twitter')
it_companies.update(['X','PTI','CFT'])
it_companies.remove('Apple')
it_companies.discard('Apple')
#when you use discard it will not give an error if the item is not present in the set but remove will give an error if the item is not present in the set
print(it_companies)

joined = A | B
inter = A & B
print(A.issubset(B))
print(A.isdisjoint(B))
diff = B - A
print(diff)

del A
del B
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

age_set = set(age)
print(f"List length: {len(age)}\nSet lenght: {len(age_set)}")

s1 = 'String is sequance of character stored at contigeous memory location and they are immutable.'
l1 = 'List is an use to store multiple data under single name and they can contain duplicate value and they are mutable.'
t1 = 'Tuple is same as list but just they are immutable.'
se1 = 'Set is unordered collection of elements and they are used to store unique elements.'

setWords = set([s1,l1,t1,se1])
print(setWords)

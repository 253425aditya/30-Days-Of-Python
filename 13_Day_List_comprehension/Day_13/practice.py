numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_neg = [i for i in numbers if i<0]

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
linear_list = [i for sublist in list_of_lists for i in sublist]

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[pair[0].upper(), pair[0][:3].upper(), pair[1].upper()] for sublist in countries for pair in sublist]

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

dicti = [{'Country' : item[0][0], 'City' : item[0][1]} for item in countries]

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

full_name = [item[0][0]+" "+item[0][1] for item in names] 
print(full_name)

nums = [i for i in range(100)]
print(nums)

print(names)
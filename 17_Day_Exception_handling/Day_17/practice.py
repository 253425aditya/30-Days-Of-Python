fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []

for f,v in zip(fruits,vegetables):
    fruits_and_veges.append((f,v))

print(fruits_and_veges)

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

*nordic_countries,es,ru = names
print(f'{nordic_countries}\n {es}\n"ru"')

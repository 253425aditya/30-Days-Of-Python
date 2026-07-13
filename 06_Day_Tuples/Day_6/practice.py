#Exercises: Level 1

tp1 = ()
t1 = ('Giang','Sol')
t2 = ('Helios','Sun')
t3 = t1 + t2
l1 = list(t1)
l1.append('Hydra')
t1 = tuple(l1)
print(t3)

#Exercises: Level 2

a,b,c = t1
print(a,b,c)
fruits = ('banana','orange','mango','lemon')
vegetables = ('Tomato','Potato','Cabbage','Onion','Carrot')
animals = ('Tiger','Lion','Puma','Leopard')

food_studd_it = fruits + vegetables + animals
print(food_studd_it)
print(food_studd_it[len(food_studd_it)//2])
print(food_studd_it[:3])
print(food_studd_it[-3:])

del food_studd_it

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
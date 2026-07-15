# age = int(input("Enter your age: "))
# if age >= 18 :
#     print("You are old enough to learn to drive.")
# else :
#     print(f"You need {18-age} more years to learn to drive.")

# num1 = int(input("Enter your num1: "))
# num2 = int(input("Enter your num2: "))
# if num1 > num2 :
#     print("Number 1 is greater Than number 2")
# else :
#     print("Number 2 is greater Than number 1")

# score = int(input("Enter you score : "))
# if score >= 90 :
#     print('A')
# elif score >= 80 :
#     print('B')
# elif score >= 70 :
#     print('C')
# elif score >= 60 :
#     print('D')
# else :
#     print('Fail')

# Autumn = ['September', 'October', 'November']
# Winter = ['December', 'January', 'February']
# Spring  = ['March', 'April', 'May']
# Summer = ['June', 'July', 'August']

# season = input("Enter a Season : ")
# season = season.capitalize()
# if season in Autumn:
#     print("Season is Autumn")
# elif season in Winter:
#     print("Season is Winter")
# elif season in Spring:
#     print("Season is Spring")
# elif season in Summer:
#     print("Season is Summer")
# else:
#     print("Enter Valid Month name")

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]
    print("Middle skill:", middle_skill)

if 'skills' in person:
    print("Has Python skill:", 'Python' in person['skills'])

if 'skills' in person:
    skills = person['skills']

    if all(skill in skills for skill in ['JavaScript', 'React']) and len(skills) == 2:
        print("He is a front end developer")

    elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']):
        print("He is a backend developer")

    elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
        print("He is a fullstack developer")

    else:
        print("Unknown title")

if person['is_married'] and person['country'] == 'Finland':
    print(
        f"{person['first_name']} {person['last_name']} lives in "
        f"{person['country']}. He is married."
    )
fruits = ['banana', 'orange', 'mango', 'lemon']
first_letter_fruits = [i[0] for i in fruits]

numbers = list(range(1,11))
print(numbers)
even_sq = [i**2 for i in numbers if i%2==0]
print(even_sq)

strings = ['1','2','3','4','5']
integer = [int(i) for i in strings]
print(type(integer[0]))


num = 12
div = [n for n in range(1,12+1) if num%n==0]
print(div)

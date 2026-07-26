import requests
import statistics

url = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(url)

print(response.status_code)

cats = response.json()

ages = []

for cat in cats:
    ages.append(int(cat["life_span"][-2:]))

print("Minimum:", min(ages))
print("Maximum:", max(ages))
print("Mean:", statistics.mean(ages))
print("Median:", statistics.median(ages))
print("Standard Deviation:", statistics.stdev(ages))

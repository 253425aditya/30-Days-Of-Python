import requests # importing the request module

url = 'https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page
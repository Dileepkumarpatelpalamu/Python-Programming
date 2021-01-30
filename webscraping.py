import requests
from bs4 import BeautifulSoup
geturl = input("Enter any url :\n")
response = requests.get(geturl)
soup = BeautifulSoup(response.text,'html.parser')
contents = soup.prettify()
print(contents)


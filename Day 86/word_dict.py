import requests

URL ='https://www.mit.edu/~ecprice/wordlist.10000'

response = requests.get(URL)
response.raise_for_status()
data = response.content.decode('utf-8').splitlines()
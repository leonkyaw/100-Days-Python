import requests

age_url = 'https://api.agify.io'
params = {
    'name':'James'
}
content = requests.get(age_url,params=params)
content.raise_for_status()
print(content.json())
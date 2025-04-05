import requests
from datetime import datetime

USER_NAME = "leonpython"
TOKEN = "applepie"
GRAPH_ID = 'graph1'
pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# Create the User
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)  # check if the registration is successful

# To create a new graph for our username

# graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
# graph_config = {
#     "id": "graph1",
#     "name": "Coding Graph",
#     "unit": "minute",
#     "type": "float",
#     "color": "ajisai",
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# To post a pixel
post_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime(year=2025, month=3, day=23)


post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "300"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(post_endpoint, json=post_params, headers=headers)
# print(response.text)

# Update the post
update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_params = {
    "quantity": "20"
}
# response = requests.put(update_endpoint,json=update_params,headers=headers)
# print(response.text)

# Delete the post
delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(delete_endpoint, headers=headers)
print(response.text)

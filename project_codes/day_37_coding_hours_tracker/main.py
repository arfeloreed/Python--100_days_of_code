import requests
from datetime import datetime

USER = "your username"
TOKEN = "token you created"

# create account
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_PARAMS = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=PIXELA_ENDPOINT, json=PIXELA_PARAMS)

date = datetime(year=2022, month=12, day=10).strftime("%Y%m%d")
today = datetime.now().strftime("%Y%m%d")
print(today)

graph_id = "graph1"
graph_params = {
    "id": graph_id,
    "name": "Hourly Coding",
    "unit": "h",
    "type": "int",
    "color": "sora",
}
header = {
    "X-USER-TOKEN": TOKEN,
}

# create a graph
graph_endpoint = f"{PIXELA_ENDPOINT}/{USER}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_params, headers=header)

# create a pixel
add_pixel_params = {
    "date": today,
    "quantity": input("How many hours did you code today? "),
}
add_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USER}/graphs/{graph_id}"
# response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=header)

# edit an existing pixel value
edit_endpoint = f"{PIXELA_ENDPOINT}/{USER}/graphs/{graph_id}/{date}"
edit_params = {
    "quantity": "7",
}
# response = requests.put(url=edit_endpoint, json=edit_params, headers=header)

# delete a pixel
delete_endpoint = f"{PIXELA_ENDPOINT}/{USER}/graphs/{graph_id}/{date}"
# response = requests.delete(url=delete_endpoint, headers=header)

# print(response.text)

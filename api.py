import requests

# #list users
# response = requests.get("https://reqres.in/api/users?page=2")
# print(response)
# print(response.json())


# #list user
# response = requests.get("https://reqres.in/api/users/2")
# print(response)
# print(response.json())

response = requests.post("https://reqres.in/api/users", {
    "name": "ugobase",
    "gender": "male"
})
print(response.json())
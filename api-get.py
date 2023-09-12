import requests

URL = "https://reqres.in"

def get_all_users():
    print("Request: Getting all users")
    #response = requests.get("https://reqres.in/api/users")
    #String Format
    response = requests.get("{}/api/users".format(URL))
    print("ResponseCode: ", response)
    print("ResponseBody", response.json())
    return response.json

base = get_all_users()

#for i in base["data"]:
    #print(i["avatar"])


def get_user(user_id):
    print("Request: Getting a user:", user_id)
    #response1 = requests.get("https://reqres.in/api/users/2")
    response1 = requests.get("{}/api/users/{}".format(URL, user_id))
    print("ResponseCode: ", response1)
    print("ResponseBody", response1.json())
    return response1.json

get_user(1)


def create_user(user_info):
    print("Request: Getting a user info:", user_info)
    response = requests.post("{}/api/users".format(URL), user_info)
    print("ResponseCode: ", response)
    print("ResponseBody", response.json())
    return response.json

create_user({
    "name": "ugobase",
    "gender": "male"
})


create_user({
    "name": "ugobase",
    "race": "black"
})



Name = "Base"
Gender = "Male"
Position = 5

print("Name: {}, Gender: {}, Position: {}".format(Name,Gender,Position))

Reply = "Hello {}".format("Ugochukwu")
print(Reply)

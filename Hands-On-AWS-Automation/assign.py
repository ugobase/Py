import boto3

client = boto3.client('iam')

#print(dir(client))

# users = ["Chike", "Ikenna", "Ugobase1", "Wow"]

# for i in users:
#     #print(i)
#     print("Creating IAM User",  i)
#     response = client.create_user(
#     #Path='string',
#     UserName= i
#     # PermissionsBoundary='string',
#     # Tags=[
#     #     {
#     #         'Key': 'string',
#     #         'Value': 'string'
#     #     },
#     # ]
# )

# print("Response Message :" , response)


users = ["Chike", "Ikenna", "Ugobase", "Wow"]

for i in users:
    print("Deleting IAM User: ",  i)
    response = client.delete_user(
    UserName= i   
)



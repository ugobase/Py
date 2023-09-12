import boto3

identity = boto3.client('iam')

print(dir(identity))

response = identity.create_user(
    #Path='string',
    UserName='Mgboji'
    # PermissionsBoundary='string',
    # Tags=[
    #     {
    #         'Key': 'string',
    #         'Value': 'string'
    #     },
    # ]
)

print(response)
import boto3

#custom_session = boto3.session.Session(profile_name = "default", region_name = "us-east-1")
Ec2 = boto3.client("ec2")

response = Ec2.describe_instances(InstanceIds=[
        'i-03fa354f25ca14cd3',
    ])

print(response)


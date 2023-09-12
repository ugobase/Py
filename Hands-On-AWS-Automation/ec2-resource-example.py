import boto3

custom_session = boto3.session.Session(profile_name = "default", region_name = "us-east-1")

#Ec2 = custom_session.resource("ec2")

Ec2 = boto3.resource("ec2")

Instance = Ec2.Instance('i-03fa354f25ca14cd3')

print(Instance.image_id)
print(Instance.state)
print(Instance.instance_id)
print(Instance.instance_type)
print(Instance.public_ip_address)

Instance.stop()
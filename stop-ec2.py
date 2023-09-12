import boto3

client = boto3.client("ec2")


##list of instances

response = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:env',
            'Values': [
                'dev', 'test', 'prod', 'terraform'
            ]
         },
         {
            'Name': 'instance-state-name',
            'Values': [
                'running', 'stopped'
            ]
         }
     ]
    
)



for i in response["Reservations"][0]["Instances"]:
    print(i["InstanceId"])
#     response = client.stop_instances(
#     InstanceIds=[
#     i["InstanceId"]
#     ]
    response = client.terminate_instances(
    InstanceIds=[
        i["InstanceId"]
    ]
 )
    #print()

#print(response["Reservations"][0]["Instances"])

#print(response.keys())

#print(response["Reservations"])

#print(len(response["Reservations"]))

#print(len(response["Reservations"][0]["Instances"]))

# for i in response["Reservations"][0]["Instances"]:
#     print(i)
#     print()


# for i in response["Reservations"][0]["Instances"]:
#     print(i["InstanceId"])


# for i in response["Reservations"][0]["Instances"]:
#     print(i["Tags"], i["InstanceId"])



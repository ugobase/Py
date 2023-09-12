import boto3

client = boto3.client('ec2')

response = client.describe_volumes(
    Filters=[
        {
            'Name': 'status',
            'Values': [
                'available',
            ]
        }
        ]
)
print(len(response["Volumes"]))

for i in response["Volumes"]:
    print(i["VolumeId"])
    print("Creation of Snapshots")
    response = client.create_snapshot(
    VolumeId=i["VolumeId"]
)
   
    print("Deletion of Volume")
    response = client.delete_volume(
    VolumeId=i["VolumeId"]
)

import boto3
import time

def lambda_handler(event, context):
    client = boto3.client('ec2')

    response = client.describe_volumes(
        Filters=[
            {
                'Name': 'status',
                'Values': [
                    'available'
                ]
            },
        ]
        
    )
    for i in response["Volumes"]:
        print()
        print("Volume info: ", i["VolumeId"])
        print("Volume info: ", i["VolumeType"])
        print("Volume info: ", i["CreateTime"])
        #print("Creation of Snapshot:", i["VolumeId"])
        print("Deletion of Volume:", i["VolumeId"])

        # response = client.create_snapshot(
        #     VolumeId= i["VolumeId"]
        # )
        # time.sleep(5)

        response = client.delete_volume(
        VolumeId= i["VolumeId"]
    )













#s3_client = boto3.client('s3')
#print(dir(s3_client))
#result = s3_client.list_buckets
#print(result)
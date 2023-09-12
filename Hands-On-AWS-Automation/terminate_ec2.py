import boto3

vm = boto3.client("ec2")

response = vm.terminate_instances(
    InstanceIds=[
        'i-03fa354f25ca14cd3',
    ]
    #DryRun=True|False
)

print(response)
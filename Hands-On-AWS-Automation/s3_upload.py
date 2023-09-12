import boto3

storage = boto3.client("s3")

storage.upload_file('./Hands-On-AWS-Automation/story.txt', 'mgbojiugochukwu7711', 'story.txt')

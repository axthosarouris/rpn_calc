import os

import boto3


def handle_request(input, context):
    s3_client = boto3.client("s3")
    s3_client.put_object(
        Body="Hello World",
        Bucket=os.environ["BUCKET_NAME"],
        Key='file.txt'
    )
    return "Hello World"

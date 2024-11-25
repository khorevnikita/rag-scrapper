import boto3

def upload_to_s3(bucket_name: str, key: str, content: str):
    s3 = boto3.client("s3")
    s3.put_object(Bucket=bucket_name, Key=key, Body=content)

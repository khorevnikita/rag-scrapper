import boto3
from config.s3 import S3_ACCESS_KEY, S3_SECRET_KEY, S3_BUCKET, S3_ENDPOINT_URL

s3_client = boto3.client(
    's3',
    endpoint_url=S3_ENDPOINT_URL,
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY
)


def upload_to_s3(key: str, content: str):
    s3_client.put_object(Bucket=S3_BUCKET, Key=key, Body=content)


def download_from_s3(key: str) -> str:
    """
    Загрузка строки из S3.
    """
    obj = s3_client.get_object(Bucket=S3_BUCKET, Key=key)
    return obj["Body"].read().decode("utf-8")

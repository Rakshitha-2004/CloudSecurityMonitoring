import boto3

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

def get_buckets():
    response = s3.list_buckets()

    buckets = []

    for bucket in response["Buckets"]:
        buckets.append({
            "bucket_name": bucket["Name"]
        })

    return buckets
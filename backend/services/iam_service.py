import boto3

iam = boto3.client(
    "iam",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

def get_users():
    response = iam.list_users()

    users = []

    for user in response["Users"]:
        users.append({
            "userName": user["UserName"],
            "arn": user["Arn"]
        })

    return users
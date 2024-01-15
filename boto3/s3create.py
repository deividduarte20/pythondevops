import boto3

s3_client = boto3.client('s3')

bucket_name = 'dduarte2024'

# Cria bucket
# response = s3_client.create_bucket(
#     Bucket=bucket_name
# )

# print(response)
# print(f'Bucket S3 "{bucket_name}" criado com sucesso.')

# Deleta bucket
response = s3_client.delete_bucket(
    Bucket=bucket_name
)

print(response)
print(f'Bucket S3 "{bucket_name}" deletado com sucesso.')
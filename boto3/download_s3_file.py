import boto3

s3 = boto3.resource('s3')
s3.meta.client.download_file('dduarte2024', 'Deivid.jpg', '/tmp/Deivid.jpg')
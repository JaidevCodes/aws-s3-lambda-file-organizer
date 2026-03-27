import json
import boto3
import urllib.parse

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        record = event['Records'][0]
        bucket = record['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(record['s3']['object']['key'])

        print("NEW CODE RUNNING")
        print(f"File uploaded: {key} in bucket: {bucket}")

        # 🚫 Ignore folders (important)
        if key.endswith('/'):
            print("Folder detected. Skipping.")
            return

        # 🚫 Skip already processed files
        if key.startswith(('images/', 'documents/', 'videos/', 'others/')):
            print("File already organized. Skipping.")
            return

        # Extract file name
        file_name = key.split('/')[-1].lower()
        print(f"Detected file name: {file_name}")

        # Decide folder
        if file_name.endswith(('.jpg', '.jpeg', '.png')):
            folder = 'images/'
        elif file_name.endswith('.pdf'):
            folder = 'documents/'
        elif file_name.endswith(('.mp4', '.mov')):
            folder = 'videos/'
        else:
            folder = 'others/'

        new_key = folder + file_name

        # Copy file
        s3.copy_object(
            Bucket=bucket,
            CopySource={'Bucket': bucket, 'Key': key},
            Key=new_key
        )

        # Delete original
        s3.delete_object(
            Bucket=bucket,
            Key=key
        )

        print(f"Moved {key} → {new_key}")

        return {
            'statusCode': 200,
            'body': json.dumps('File organized successfully!')
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        raise e

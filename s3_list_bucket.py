#!/usr/bin/env python3
"""
Simple MinIO S3 bucket listing example for NRP batch jobs.
Lists top-level objects like 'mc ls' command.
"""

import os
import sys
from minio import Minio
from minio.error import S3Error


def main():
    """List S3 bucket contents using MinIO."""
    # Get credentials from environment variables
    endpoint = os.environ.get('AWS_S3_ENDPOINT')
    access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    bucket_name = os.environ.get('S3_BUCKET_NAME', 'my-bucket')
    
    # Validate required environment variables
    if not access_key or not secret_key or not endpoint:
        print("❌ Error: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_S3_ENDPOINT must be set")
        sys.exit(1)
    
    try:
        # Initialize MinIO client
        client = Minio(endpoint, access_key=access_key, secret_key=secret_key, secure=True)
        
        # List top-level objects in the bucket (like mc ls)
        objects = client.list_objects(bucket_name, recursive=False)
        
        print(f"Contents of {bucket_name}:")
        for obj in objects:
            print(f"  {obj.object_name}")
        
    except S3Error as e:
        print(f"❌ S3 Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

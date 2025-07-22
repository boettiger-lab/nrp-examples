#!/usr/bin/env python3
"""
MinIO S3 bucket listing example for NRP batch jobs.

This script demonstrates how to use MinIO client to list contents of an S3 bucket
on the National Research Platform (NRP) using Kubernetes batch jobs with secrets.
"""

import os
import sys
from minio import Minio
from minio.error import S3Error


def main():
    """Main function that lists S3 bucket contents using MinIO."""
    print("=" * 50)
    print("🪣 MinIO S3 Bucket Listing Example")
    print("=" * 50)
    
    # Get credentials from environment variables
    endpoint = os.environ.get('AWS_S3_ENDPOINT')
    access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    bucket_name = os.environ.get('S3_BUCKET_NAME', 'my-bucket')
    
    # Validate required environment variables
    if not access_key or not secret_key:
        print("❌ Error: AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY must be set")
        sys.exit(1)
    
    if not endpoint:
        print("❌ Error: AWS_S3_ENDPOINT must be set")
        sys.exit(1)
    
    print(f"🔗 Endpoint: {endpoint}")
    print(f"🪣 Bucket: {bucket_name}")
    print(f"🔑 Access Key: {access_key[:4]}***{access_key[-4:] if len(access_key) > 8 else '***'}")
    
    try:
        # Initialize MinIO client
        client = Minio(
            endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=True  # Use HTTPS
        )
        
        print(f"\n📋 Listing objects in bucket '{bucket_name}':")
        print("-" * 40)
        
        # List objects in the bucket
        objects = client.list_objects(bucket_name, recursive=True)
        
        count = 0
        total_size = 0
        
        for obj in objects:
            count += 1
            size_mb = obj.size / (1024 * 1024) if obj.size else 0
            total_size += obj.size if obj.size else 0
            
            print(f"{count:3d}. {obj.object_name}")
            print(f"     Size: {size_mb:.2f} MB | Last Modified: {obj.last_modified}")
        
        if count == 0:
            print("     (No objects found)")
        else:
            total_size_mb = total_size / (1024 * 1024)
            print("-" * 40)
            print(f"📊 Total: {count} objects, {total_size_mb:.2f} MB")
        
        print("\n✅ Bucket listing completed successfully!")
        
    except S3Error as e:
        print(f"❌ S3 Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)
    
    print("=" * 50)


if __name__ == "__main__":
    main()

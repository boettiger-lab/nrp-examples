# nrp-examples

Examples for running jobs on the National Research Platform (NRP) using Kubernetes.

## MinIO S3 Bucket Listing Example

This repository contains a Python script that demonstrates how to list contents of an S3 bucket using the MinIO client library in NRP batch jobs.

### Files

- `s3_list_bucket.py` - A Python script that uses MinIO to list S3 bucket contents
- `requirements.txt` - Python dependencies (MinIO client library)
- `batch.yaml` - Kubernetes batch job configuration that runs the S3 listing script
- `create_secret.sh` - Helper script to create AWS credentials secret

### Prerequisites

Before running the example, you need to create a Kubernetes secret with your AWS credentials:

```bash
kubectl create secret generic aws-credentials \
  --from-literal=access-key-id=YOUR_ACCESS_KEY \
  --from-literal=secret-access-key=YOUR_SECRET_KEY
```

### Configuration

You can customize the MinIO endpoint and bucket name by editing the environment variables in `batch.yaml`:

- `AWS_S3_ENDPOINT`: The MinIO endpoint (e.g., your-minio-server.com:9000)
- `S3_BUCKET_NAME`: The bucket name to list (default: my-test-bucket)

### Running the Example

To run the MinIO S3 example on NRP:

1. Create the AWS credentials secret (see Prerequisites above)

2. Apply the batch job configuration:
   ```bash
   kubectl apply -f batch.yaml
   ```

3. Check the job status:
   ```bash
   kubectl get jobs
   ```

4. View the output logs:
   ```bash
   kubectl logs job/myapp
   ```

5. Clean up the job when done:
   ```bash
   kubectl delete -f batch.yaml
   ```

### What the Script Does

The `s3_list_bucket.py` script:
- Installs Python dependencies from requirements.txt at runtime
- Reads AWS credentials from Kubernetes secrets
- Connects to the specified S3 endpoint
- Lists all objects in the specified bucket
- Shows object names, sizes, and modification dates
- Provides summary statistics

This demonstrates how to:
- Manage Python dependencies with requirements.txt
- Use external Python packages in NRP jobs
- Handle sensitive credentials securely with Kubernetes secrets
- Work with cloud storage from batch jobs
- Provide detailed logging and error handling

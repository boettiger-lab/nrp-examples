#!/bin/bash
# create_secret.sh - Helper script to create AWS credentials secret for NRP batch jobs

echo "Creating AWS credentials secret for NRP batch jobs..."
echo

# Prompt for AWS credentials
read -p "Enter your AWS Access Key ID: " ACCESS_KEY
read -s -p "Enter your AWS Secret Access Key: " SECRET_KEY
echo
echo
echo "Note: Update the AWS_S3_ENDPOINT in batch.yaml to point to your MinIO server"
echo "Example: your-minio-server.com:9000"
echo

# Validate inputs
if [[ -z "$ACCESS_KEY" || -z "$SECRET_KEY" ]]; then
    echo "❌ Error: Both Access Key ID and Secret Access Key are required"
    exit 1
fi

# Create the secret
echo "Creating Kubernetes secret 'aws-credentials'..."
kubectl create secret generic aws-credentials \
  --from-literal=access-key-id="$ACCESS_KEY" \
  --from-literal=secret-access-key="$SECRET_KEY"

if [[ $? -eq 0 ]]; then
    echo "✅ Secret 'aws-credentials' created successfully!"
    echo
    echo "You can now run the batch job with:"
    echo "  kubectl apply -f batch.yaml"
else
    echo "❌ Failed to create secret"
    exit 1
fi

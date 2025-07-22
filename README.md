# nrp-examples

Examples for running jobs on the National Research Platform (NRP) using Kubernetes.

## Hello World Example

This repository contains a simple hello world Python script that demonstrates how to run batch jobs on the NRP.

### Files

- `hello_world.py` - A simple Python script that prints system information and environment details
- `batch.yaml` - Kubernetes batch job configuration that runs the hello world script

### Running the Example

To run the hello world example on NRP:

1. Apply the batch job configuration:
   ```bash
   kubectl apply -f batch.yaml
   ```

2. Check the job status:
   ```bash
   kubectl get jobs
   ```

3. View the output logs:
   ```bash
   kubectl logs job/myapp
   ```

4. Clean up the job when done:
   ```bash
   kubectl delete -f batch.yaml
   ```

### What the Script Does

The `hello_world.py` script:
- Prints a welcome message
- Shows current timestamp
- Displays Python version and system information
- Lists environment variables
- Shows command line arguments
- Lists files in the current directory

This provides useful debugging information to verify that your job is running correctly on the NRP infrastructure.

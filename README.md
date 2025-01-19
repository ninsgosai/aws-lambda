# Lambda Example for Python error log find from log files 

Copy the Lambda Function code from lambda_function.py

Use the AWS Management Console or AWS CLI to create a new Lambda function.
Choose Python 3.9+ runtime.
Set the memory to 128 MB and timeout to 30 seconds.
Attach the basic Lambda execution role.
# Deploy the Code

Copy the above Lambda function code into the editor in the AWS Management Console or upload it as a .zip package.
Create a Test Event:

Use the following as a test event in AWS:

{
  "candidate_id": "YOUR_ID",
  "log_content": "[2024-01-07 10:15:30] ERROR: Database connection failed\n[2024-01-07 10:15:35] INFO: Retry attempt 1"
}


# API Gateway Configuration:

Create a REST API in API Gateway.
Define an endpoint (e.g., /process-logs) and link it to the Lambda function.
Deploy the API and note the endpoint URL.



Test the Lambda function using AWS-provided test cases or Postman.
To test this lambda we have process_log_file.py file run it with nacessary parameters
For Postman, send a POST request to the API Gateway endpoint.

# Edge Case Testing:
Test with empty logs and malformed entries to ensure robustness.

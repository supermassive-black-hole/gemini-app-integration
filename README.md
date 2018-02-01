# Integration Example for the Gemini App

This code is a fully deployable demo application integrating the face/id matchineg [gemini application](https://www.gemini-app.ai).
It is programmed with the [AWS Serverless Application Model](https://github.com/awslabs/serverless-application-model). To use it, follow these 10 steps.

1. Log into your Gemini profile and copy the API Key.
2. Log In your AWS account or create one if necessary.
3. In 'Services → EC2 → Parameter Store', create a `SecureString` parameter with the name `/gemini-app-integration/api-key` and
   your API Key as a value. Use the default encryption key named `alias/aws/ssm` that AWS creates for you automatically.
4. In 'Services → S3', create an S3 bucket for AWS SAM to deploy the code
5. In 'Services → IAM → Encryption keys → <your aws region>', copy the ID of the encryption key `aws/ssm` that you used
   above to create the secure parameter.
6. If you do not have it, install the `awscli` command line tool of AWS.
7. Execute the following command by filling in the name of your s3 bucket and the id of the encryption key
```
S3_BUCKET_NAME=<s3_bucket> S3_PREFIX=gemini-app-integration/code KMS_KEY_ID=<id_of_aws_ssm_key> STACK_NAME=gemini-app-integration ./deploy.sh
```
8. In 'Services → API Gateway', choose the api you just created with the command above, it is called `gemini-app-integration` like the stack you created
   in step 7.
9. Under 'Stages', choose the `Prod` stage and follow the URL to test the gemini application.
10. To delete the installed application, go to 'Services → Cloudformation'

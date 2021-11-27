# AWS Lambda Authorizer

This is a template serverless application used for authorizing to AWS Cognito.

# Setup

1. Configure aws-cli.
2. Create a Cognito User Pool with an Identity Pool.
4. Create a parameter in Parameter Store containing the App Client id. The name must be "CLIENT_ID_SSM_PARAMETER_NAME" or you may change it.
3. Create an App Client for the User Pool.
5. Deploy with `sls deploy`.

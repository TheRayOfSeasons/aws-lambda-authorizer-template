import json
import logging
import os

import boto3

from utils.ssm import get_parameter_from_ssm


AWS_REGION = os.getenv('AWS_REGION')
AWS_COGNITO_IDENTITY_POOL = boto3.client('cognito-idp', region_name=AWS_REGION)
CLIENT_ID_SSM_PARAMETER_NAME = os.getenv('CLIENT_ID_SSM_PARAMETER_NAME')
USER_POOL_CLIENT_ID = get_parameter_from_ssm(CLIENT_ID_SSM_PARAMETER_NAME)


def authenticate(event, context):
    """
    Authenticates to AWS Cognito's Identity Pool then
    returns the user's access tokens if valid.
    """
    parameters = json.loads(event['body'])
    response = AWS_COGNITO_IDENTITY_POOL.initiate_auth(
        ClientId=USER_POOL_CLIENT_ID,
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters=parameters
    )
    if response.get('AuthenticationResult'):
        access_token = response['AuthenticationResult']['AccessToken']
        response['User'] = AWS_COGNITO_IDENTITY_POOL.get_user(
            AccessToken=access_token
        )
    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }

import boto3
import json

ssm = boto3.client('ssm')


def lambda_handler(event, context):
    try:
        request_body = json.loads(event['body'])
        parameter_name = request_body.get('parameter_name')
    except (json.JSONDecodeError, KeyError):
        return {
            'statusCode': 400,
            'body': 'Invalid request body'
        }

    if not parameter_name:
        return {
            'statusCode': 400,
            'body': 'Parameter name not provided in request body'
        }
    try:
        response = ssm.get_parameter(Name=parameter_name, WithDecryption=True)
        parameter_value = response['Parameter']['Value']
    except ssm.exceptions.ParameterNotFound:
        return {
            'statusCode': 404,
            'body': f'SSM Parameter not found: {parameter_name}'
        }

    return {
        'statusCode': 200,
        'body': f'SSM Parameter Value: {parameter_value}'
    }

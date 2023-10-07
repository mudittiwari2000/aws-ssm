import boto3


def lambda_handler(event, context):
    parameter_name = print(event)
    ssm_client = boto3.client('ssm')

    parameter_name = 'YourParameterNameHere'

    try:
        # Query the SSM parameter
        response = ssm_client.get_parameter(
            Name=parameter_name, WithDecryption=True)
        parameter_value = response['Parameter']['Value']
        return parameter_value
    except Exception as e:
        return str(e)

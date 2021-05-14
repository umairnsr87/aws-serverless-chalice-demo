"""
All the helper functions will come here
"""

def invoke_lambda_function(function_name,invocation_type, data):
    """
    function_name : name of the function
    invocation_type : type of invocation
    data : dictionary of required parameters

    """
    import json
    import boto3
    client = boto3.client('lambda')
    response=client.invoke(
        FunctionName=function_name,
        InvocationType=invocation_type,
        Payload=json.dumps(data),
    )
    return response

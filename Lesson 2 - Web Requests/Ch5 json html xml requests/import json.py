import json
import boto3
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # TODO implement
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_file_name = event['Records'][0]['s3']['object']['key']

    json_object = s3_client.getObject(Bucket=bucket,Key=json_file_name)
    jsonFileReader = json_object['Body'].read()
    jsonDict = json.loads(jsonFileReader)
    
    table = dynamodb.Table('games')
    table.put_item(Item=jsonDict)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(json_object)
    }

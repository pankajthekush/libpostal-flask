import json

def lambda_handler(event, context):
    body = event['body']

    return {
      'statusCode': 200,
      'body': json.dumps({"Message": "Forbidden"})
      }
import json
import pymysql

def lambda_handler(event, context):
    # TODO implement
    print("success pymysql")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    

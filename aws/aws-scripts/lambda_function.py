import json
import boto3
import time
from datetime import datetime

def lambda_handler(event, context):
    client = boto3.resource("dynamodb")
    table = client.Table("foralltimesDB")
    
    data_raw = table.scan()['Items']
    data_json = data_raw[0]
    
    old_count = data_json['counter']
    
    diff = event['update']

    
    
    table.put_item(Item={'id':1, 'counter': old_count + diff, 'time': "{}".format(datetime.now())})
    return None
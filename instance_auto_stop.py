#-*- coding: utf-8 -*-

# Stops all instances of all regions that are not Stop protection tagged.
# Stop Protect Tag name is 'AutoStopProtect'. Value 'True' is only valid.
# Target runtime is Python 3.6 or higher.
# Timeout is recommended for 1 minute or longer.

import boto3
import logging

# setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('ec2')

runningInstanceFilter = [
    {
        'Name': 'instance-state-name',
        'Values': ['running']
    }
]

def lambda_handler(event, context):
    
    instances = []
    for region in client.describe_regions()['Regions']:
        # define the connection
        ec2 = boto3.resource('ec2', region_name=region['RegionName'])
    
        # filter the running instances
        instances = ec2.instances.filter(Filters=runningInstanceFilter)
    
        for instance in instances:
            shuttingDownFlag = True
            for tags in instance.tags:
                # Stop Protect Key name is AutoStopProtect. Only 'True' is valid.
                if tags["Key"] == 'AutoStopProtect' and tags["Value"] == 'True':
                    shuttingDownFlag = False
    
            if shuttingDownFlag == True:
                shuttingDown = instance.stop()
                print(shuttingDown)
from __future__ import print_function
import boto3
import logging
import datetime
from datetime import date


def lambda_handler(event, context):
    
	#CHANGE 
    regions = ["region1", "region2"]
    
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)
        ec2client = boto3.client('ec2', region_name=region)
        response = ec2client.describe_instances()
        # print(response)
        
		#CHANGE 
        my_images = ec2.images.filter(Owners=[ACCOUNT_ID])
        for image in my_images:
            for tags in image.tags:
                if tags["Key"] == 'RemoveOn':
                    #If today is the removal date, terminate it
                    if tags['Value'] == date.today().strftime('%d-%m-%Y'):
                        print("Deregistering " + image.id + " in " + region)
                        ec2client.deregister_image(ImageId=image.id)
            
        for instance in ec2.instances.all():
            for tags in instance.tags:
                #If instance has a specific removal date
                if tags["Key"] == 'RemoveOn':
                    #If today is the removal date, terminate it
                    if tags['Value'] == date.today().strftime('%d-%m-%Y'):
                        print("Terminating EC2 " + instance.id + " in " + region)
                        ec2.Instance(instance.id).stop()
                        #print(ec2.Instance(instance.id).stop())

import boto3
from datetime import datetime, timedelta

# You need to specify the AWS region
region = 'us-west-1'

# Create a session using your AWS credentials
session = boto3.Session(region_name=region)

# AWS resource and client
ec2_resource = session.resource('ec2')
ec2_client = session.client('ec2')

# Calculate the date 3 months ago
three_months_ago = datetime.now() - timedelta(90)

def delete_snapshots():
    for snapshot in ec2_resource.snapshots.filter(OwnerIds=['self']):
        if snapshot.start_time < three_months_ago:
            print(f"Deleting snapshot {snapshot.snapshot_id}")
            snapshot.delete()

delete_snapshots()

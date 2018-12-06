import boto3
region = 'us-east-1'


def lambda_handler(tagkey, tagvalue):

    ec2client = boto3.client('ec2')

    response = ec2client.describe_instances(
        Filters=[
            {
                'Name': 'tag:'+'Name',
                'Values': ['Jenkins']
            }
        ]
    )
    instancelist = []
    for reservation in (response["Reservations"]):
        for instance in reservation["Instances"]:
            instancelist.append(instance["InstanceId"])
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instancelist)
    print 'stopped your instances: ' + str(instancelist)
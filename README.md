awswrapper - AWS API Wrapper 
========================

AWS API Wrapper for Lambda

Usage
-----

It will look into your aws credentials file

Import the ec2wrapper

    >>> from awswrapper import ec2wrapper

Use describe functions for talk to aws

    >>> ec2wrapper.describe_instances(state=None)
    >>> ec2wrapper.describe_instances_by_tag(tag, value=None, state=None)
    
Execute actions on those Instances

    >>> ec2wrapper.terminate_instances(instance_ids, dry_run)
    >>> ec2wrapper.stop_instances(instance_ids, dry_run)
    >>> ec2wrapper.start_instances(instance_ids, dry_run)

Get data from the EC2 Response

    >>> ec2wrapper.get_instances_data(ec2_instances)
    >>> ec2wrapper.get_instances_ids(ec2_instances)
    
Get data from Instance

    >>> ec2wrapper.get_tags_from_instance(instance)
    
Get the EC2 Connection

    >>> ec2wrapper.get_ec2_connection(instance)

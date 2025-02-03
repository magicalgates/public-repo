import boto3
import os
import json


from botocore.exceptions import ClientError


codepipeline = boto3.client('codepipeline')
ecs          = boto3.client('ecs')
ssm          = boto3.client('ssm')


try:
    INSTANCE_ID  = os.getenv('INSTANCE_ID')
    WORKING_DIR  = os.getenv('WORKING_DIR')
    ENV_NAME     = os.getenv('ENV_NAME')
    APPLICATION  = os.getenv('APPLICATION')
    LOGGROUPNAME = os.getenv('LOGGROUPNAME')
except KeyError as ke:
    print(ke)
except Exception as e:
    print(e)


def put_job_failure(job_id, message):
    try:
        codepipeline.put_job_failure_result(
            jobId=job_id,
            failureDetails={'type': 'JobFailed', 'message': message}
        )
    except ClientError as ce:
        print(ce)
        return False
    except Exception as e:
        print(e)
        return False


def put_job_success(job_id):
    try:
        codepipeline.put_job_success_result(jobId=job_id)
    except ClientError as ce:
        print(ce)
        return False
    except Exception as e:
        print(e)
        return False


def ecs_list_tasks(cluster, service):
    try:
        response = ecs.list_tasks(
            cluster=cluster,
            serviceName=service
        )
        return response['taskArns']
    except ClientError as ce:
        print(ce)
        return False
    except Exception as e:
        print(e)
        return False


def ecs_stop_task(cluster, task):
    try:
        ecs.stop_task(
            cluster=cluster,
            task=task,
            reason='Stopped by CodePipeline Lambda'
        )
        return True
    except ClientError as ce:
        print(ce)
        return False
    except Exception as e:
        print(e)
        return False


def send_ssm_command(instance_id, command):
    
    command_to_run = "/bin/su -c '" + command + "' ubuntu"

    try:
        response = ssm.send_command(
            InstanceIds=[instance_id],
            DocumentName='AWS-RunShellScript',
            Parameters={
                'commands': [command_to_run],
                'workingDirectory': WORKING_DIR,
                'executionTimeout': ["14400"]
            },
            CloudWatchOutputConfig={
                'CloudWatchLogGroupName': LOGGROUPNAME,
                'CloudWatchOutputEnabled': True
            },
            TimeoutSeconds=30
        )
        return response['Command']
    except ClientError as ce:
        print(ce)
        return False
    except Exception as e:
        print(e)
        return False


def lambda_handler(event, context):
    try:
        print("Received event: " + str(event))
        job_id          = event['CodePipeline.job']['id']
        user_parameters = json.loads(event['CodePipeline.job']['data']['actionConfiguration']['configuration']['UserParameters'])

        service_name = user_parameters["serviceName"]
        cluster      = user_parameters["clusterName"]

        if service_name == None:
            put_job_failure(str(job_id), "Service name is not specified")
            return True
        elif cluster == None:
            put_job_failure(str(job_id), "Cluster is not specified")
            return True

        command = None
        ecs_tasks = ecs_list_tasks(cluster, service_name)
        if ecs_tasks:
            print("ECS Task List Arns:", str(ecs_tasks))
            for arn in ecs_tasks:
                ecs_stop_task(cluster, arn)
        else:
            print("No running tasks to stop for service ", str(service_name))
        put_job_success(job_id)
    except ClientError as ce:
        print(ce)
        put_job_failure(str(job_id), str(ce))
    except Exception as e:
        print(e)
        put_job_failure(str(job_id), str(e))
        
    return True
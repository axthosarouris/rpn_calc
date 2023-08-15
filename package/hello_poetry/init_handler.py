import boto3


def handle_request(event, context):
    code_pipeline = boto3.client('codepipeline')
    jobId = event.get("CodePipeline.job").get("id")
    code_pipeline.put_job_success_result(jobId=jobId)

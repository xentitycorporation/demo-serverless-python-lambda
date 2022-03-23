import os
import sys
import boto3
import json
from pybars import Compiler
import requests
from smart_open import open

# Required for lambda relative pathing
sys.path.append(os.path.join(os.path.dirname(__file__)))
from lib.helpers import helpers

compiler = Compiler()

def handler(event, context):
    sourceFileTpl = compiler.compile(event['baseUrl'])
    sourceFile = sourceFileTpl(event['params'], helpers=helpers, partials={})

    destinationFileTpl = compiler.compile(event['destination']['key'])
    destinationFile = destinationFileTpl(event['params'], helpers=helpers, partials={})

    print('Downloading file from:', sourceFile)
    print('Files will be saved as:', destinationFile)

    s3url = f"s3://{event['destination']['bucket']}/{destinationFile}"
    session = boto3.Session()
    transport_params = {
        'client': session.client('s3')
    }

    try:
        response = requests.get(sourceFile, stream=True)
        with open(s3url, 'wb', transport_params=transport_params) as fout:
            bytes_written = fout.write(response.content)
            print('Total Bytes written:', bytes_written)

        print('Sucessfully saved to S3 located at:', s3url)

        return {
            'statusCode': 200,
            'body': json.dumps('Success')
        }
    except ValueError as e:
        print("An exception occurred:", e)
        return {
            'statusCode': 400,
            'body': json.dumps('Failure')
        }


from cgi import test
import json
from pprint import pprint
import re
from flask import Flask, render_template, request, redirect
import requests
import mysql.connector


import boto3
import base64
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "arn:aws:secretsmanager:us-east-1:050670689537:secret:MySQLSecret-Yi8HOWf73VGT-SzCika"
    region_name = "us-east-1"
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise e
    else:
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            res = json.loads(secret)
            pprint(res)
            return res
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            
get_secret()
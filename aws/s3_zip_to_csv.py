#!/bin/python3
# Author: Sebastian Opiyo
# Purpose: A script that runs basic aws sql database to csv tasks on Linux bash
# Date Created: Sep 29, 2020 11:54
# Date Modified: Sep 29, 2020 11:54

import json
import boto3
from io import BytesIO
import zipfile


def lambda_handler(event, context):
    s3_resource  = boto3.resource('s3')
    # Confirm whether the 's3//' has any bugy effect.
    source_s3_bucket = 's3://staging-area-innovative'
    target_s3_bucket = 's3://innovative-results-bucket-dp1'

    zip_bucket = s3_resource.Bucket(source_s3_bucket)

    for file in zip_bucket.objects.all():
        # We check if the contents of the bucket is/are zipped
        if(str(file.key).endswith('.zip')):
            zip_object = s3_resource.Object(bucket_name=source_s3_bucket, key=file.key)
            buffer = BytesIO(zip_object.get()["Body"].read())
            z = zipfile.ZipFile(buffer)
            for filename in z.namelist():
                file_info = z.getinfo(filename)
                try:
                    response = s3_resource.meta.client.upload_fileobj(
                        z.open(filename),
                        Bucket=target_s3_bucket,
                        Key=f'{filename}'
                    )
                except Exception as e:
                    print(e)
        else:
            print(file.key+ ' is not a zip file.')


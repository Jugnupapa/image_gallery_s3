import boto3
from pathlib import Path
from Gallery.settings import MEDIA_ROOT
obj = boto3.client("s3")
# Uploading a png file to S3 in 
# 'mygfgbucket' from local folder
obj.upload_file(
    Filename=MEDIA_ROOT.joinpath("pics/adam-kool-ndN00KmbJ1c-unsplash.jpg"),
    Bucket="my-staticfiles-bucket-django",
    Key="first.jpg"
)
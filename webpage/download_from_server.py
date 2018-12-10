import boto3
import time

session = boto3.Session(aws_access_key_id="AKIAJSCUUGUNFZNZEOHQ", aws_secret_access_key="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", region_name="ap-northeast-2")
s3 = session.resource('s3')

bucket_name = "dlatltkwls"
my_bucket = s3.Bucket(bucket_name)
#print(str(my_bucket))

def returnName(filename):
    a = []
    a.append(filename)

    return a

def load_image():
    a = []
    for s3_file in my_bucket.objects.all():
        if(not s3_file):
            break
        a.append(s3_file.key)
        my_bucket.download_file(s3_file.key, s3_file.key) #(다운받을 파일 이름, 다운받게 될 경로와 파일이름)
        s3.Object(bucket_name, s3_file.key).delete()

    return a
from boto3.session import Session
import argparse
import sys
import os

#Specify -h to know the input parameters
try:
    arg1 = sys.argv[1]
except IndexError:
    print "Usage: " + "python" + os.path.basename(__file__) + " -h"
    sys.exit(1)

parser = argparse.ArgumentParser()

parser.add_argument('-list',action='store_true',help="List the files in aws S3")
parser.add_argument('-download',action='store_true',help="Download the files in AWS S3")

ACCESS_KEY='XXXXXXXYYYY'
SECRET_KEY='XXXUUUHHTTTT'
args = parser.parse_args()
if args.list:
    session = Session(aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
    s3 = session.resource('s3')
    your_bucket = s3.Bucket('AA***HHHHHH')
    for s3_file in your_bucket.objects.all():
        print(s3_file.key)

if args.download:
    file = str(input('File to download specify with "XXX": '))
    session = Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    s3 = session.resource('s3')
    your_bucket = s3.Bucket('AAKKOOUUYY^^^')
    for s3_file in your_bucket.objects.all():
        your_bucket.download_file(file,file)




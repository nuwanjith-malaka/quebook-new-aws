from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
import requests
IMDSv2_TOKEN = requests.put('http://169.254.169.254/latest/api/token', headers={'X-aws-ec2-metadata-token-ttl-seconds': '3600'}).text
EC2_PRIVATE_IP = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4', timeout=0.01, headers={'X-aws-ec2-metadata-token': IMDSv2_TOKEN}).text
ELB_DNS = 'Quebook-test-web-elb-315417778.us-east-1.elb.amazonaws.com'
var1 = ELB_DNS
var2 = 'public DNS of ec2 instance'
allowed_host = var1
ALLOWED_HOSTS = [allowed_host]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

db_host = ssm_client.get_parameter(Name='DB_HOST', WithDecryption=True)['Parameter']['Value']
db_password = ssm_client.get_parameter(Name='DB_PASSWORD', WithDecryption=True)['Parameter']['Value']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'malakadb1',
        'USER': 'postgres',
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': '5432',
    }
}

LOGIN_REDIRECT_URL = 'http://' + allowed_host + '/'
LOGIN_URL = 'http://' + allowed_host + '/login/'
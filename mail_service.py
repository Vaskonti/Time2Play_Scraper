import boto3

from dotenv import dotenv_values
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('templates/'),
    autoescape=select_autoescape(['html', 'xml'])
)
ses_client = boto3.client('ses')
config = dotenv_values(".env")


def load_html_file(file_path):
    return env.get_template(file_path)


def send_email(subject, body):
    ses_client.send_email(
        Destination={
            'ToAddresses': config['RECEIVERS_TIME2PLAY'].split(",")
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': "UTF-8",
                    'Data': body,
                },
            },
            'Subject': {
                'Charset': "UTF-8",
                'Data': subject,
            },
        },
        Source=config['EMAIL_SENDER'],
        SourceArn=config['EMAIL_SENDER_ARN'],
    )

#!/bin/bash

# This script is used to upload the .env file to the S3 bucket
aws s3 cp /home/ubuntu/scripts/Time2Play_Scraper/.env.prod s3://scraper-env/.env

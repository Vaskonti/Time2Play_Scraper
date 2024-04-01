#!/bin/bash

# This script is used to upload the .env file to the S3 bucket
aws s3 cp .env.prod s3://scraper-env/.env

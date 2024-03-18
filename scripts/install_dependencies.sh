#!/bin/bash

cd /home/ubuntu/scripts/Time2Play_Scraper
pip install -r requirements.txt
aws s3 cp s3://scraper-env/.env /home/ubuntu/scripts/Time2Play_Scraper/.env


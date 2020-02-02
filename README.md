# Road-Api
In order to use this api visit ```https://foajjujxfh.execute-api.eu-west-2.amazonaws.com/Prod/{local_authority_id}/{road_name}``` the api will then return a subset of the data with that local authority and road name

## Deployment

Run ```road-api/deploy.sh <artefact_bucket>``` with valid AWS credentials

## Solution
I packaged up the csv file into the lambda which is then connected via an Api gateway, written in [SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) and python for aws. This will allow get methods and have lambda read the file. I would reconmmend a dynamo db table to keep the data in production and update the pyhon accordingly.
#!/usr/bin/env bash

#deploys the api, these steps could easily be put into a pipeline of choosing
ARTEFACT_BUCKET=$1
sam build

# go into the sam build directory
cd .aws-sam/build
sam package --template-file ./template.yaml --s3-bucket ${ARTEFACT_BUCKET} --output-template-file ./packaged.yaml
sam deploy --template-file ./packaged.yaml --stack-name road-api --capabilities  CAPABILITY_IAM

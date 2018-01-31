#!/usr/bin/env bash

set -e

rm -fr target
mkdir target

aws cloudformation package \
  --template-file template.yml \
  --s3-bucket ${S3_BUCKET_NAME} \
  --s3-prefix ${S3_PREFIX}  \
  --output-template-file target/packaged-template.yml

aws cloudformation deploy \
  --template-file target/packaged-template.yml \
  --capabilities CAPABILITY_IAM \
  --stack-name ${STACK_NAME} \
  --parameter-overrides KmsKeyId=${KMS_KEY_ID}

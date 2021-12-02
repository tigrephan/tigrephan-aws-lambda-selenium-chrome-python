Tested and working on commit date.

Working Docker container with PYTHON, Selenium, and Chrome to use with AWS Lambda

Based on https://github.com/aws-samples/serverless-ui-testing-using-selenium but simplified

Prereqs:
Git
Docker
AWS Account
AWS ECR


Instructions

1) Git clone this repo
2) Docker Build  : docker build -t lambda-selenium-chrome .
3) Run Container : docker run -p 9000:8080 <your container>
4) Test locally  : curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}' 
5) Push to AWS ECR
  
 

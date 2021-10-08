# anohana

![alt text](https://github.com/subramani-tejas/aws/anohana.jpg?raw=true)

1. Policy --> anohana | CloudWatch Logs & DynamoDB
2. Role --> anohana_Role | attach policy
3. Lambda function --> anohana_LF
   - attach role
   - logic to handle GET & POST request
4. API Gateway --> anohana_API
   - GET route
   - POST route
5. DynamoDB

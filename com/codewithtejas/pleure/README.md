# pleure

![alt text](https://github.com/subramani-tejas/aws/blob/main/com/codewithtejas/pleure/initial%20POST.png?raw=true)

1. Policy | pleure_un_policy | for both lambdas
   - CloudWatch logs - ALL
   - SQS - ALL
2. Role | pleure_un_role | attach policy
3. Lambda function | function_un
   - assume role - pleure_un_role
   - in POST call,
     - if no queue --> create queue pleure_queue

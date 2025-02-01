# public-repo

List of projects:

Project-1 : Optimized Cron: 
**Upgraded the infrastructure** by replacing traditional **EC2-based cron job scheduling** with a **serverless solution**. Utilized **AWS CloudFormation**, **AWS Lambda**, **Systems Manager**, and **EventBridge** to automate the process based on **client requirements**. At a specified time (e.g., **Eastern Time**).
**EventBridge triggers Lambda**, which **scales out the required servers** using **Auto Scaling Groups**. Once the server is available, the **Systems Manager** is used to **initiate the cron jobs**. After the jobs are completed, the server is **automatically terminated**, leading to **significant cost savings** by reducing the need for **always-on EC2 instances**. This solution improved **scheduling flexibility**, **eliminated manual cron job maintenance**, and **optimized resource utilization**.

Project-2 : Centralized logging system for AWS CloudWatch Logs:
Implemented a **centralized logging system** by setting up a **security account** to collect logs from all other AWS accounts using **CloudWatch Subscription Filters**. Logs were then streamed through **Kinesis** to **Splunk**, where specific log groups were forwarded for **analysis** and **monitoring**. This setup enhanced **log aggregation**, **security**, and **centralized monitoring** across multiple AWS accounts.


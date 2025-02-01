# public-repo

Overview of AWS Infrastructure Solutions Designed, Developed, and Implemented Across Live Projects, Integrated with 3rd-Party Tools for Enhanced Visibility, Security, Monitoring, and Scalability.

### 1. Optimized Cron
**Upgraded the infrastructure** by replacing traditional **EC2-based cron job scheduling** with a **serverless solution**. Utilized **AWS CloudFormation**, **AWS Lambda**, **Systems Manager**, and **EventBridge** to automate the process based on **client requirements**. At a specified time (e.g., **Eastern Time**).
**EventBridge triggers Lambda**, which **scales out the required servers** using **Auto Scaling Groups**. Once the server is available, the **Systems Manager** is used to **initiate the cron jobs**. After the jobs are completed, the server is **automatically terminated**, leading to **significant cost savings** by reducing the need for **always-on EC2 instances**. This solution improved **scheduling flexibility**, **eliminated manual cron job maintenance**, and **optimized resource utilization**.

### 2. Centralized logging system for AWS CloudWatch Logs
Implemented a **centralized logging system** by setting up a **security account** from **AWS Organizations** to collect logs from all other AWS accounts using **CloudWatch Subscription Filters**. Logs were then streamed through **Kinesis** to **Splunk**, where specific log groups were forwarded for **analysis** and **monitoring**. This setup enhanced **log aggregation**, **security**, and **centralized monitoring** across multiple AWS accounts.

### 3. Custom CloudWatch Metrics
Developed custom **CloudWatch metrics** using **Log Metric Filters** to monitor **Sidekiq jobs**. Implemented a **Step Scaling policy** for **Auto Scaling Groups** to automatically scale the infrastructure based on **job load**, ensuring optimal **processing capacity** during high job volumes. This solution improved system **efficiency** and **resource utilization** by dynamically adjusting the number of **instances** based on real-time **job demands**.

### 4. Automated Domain Creation with AWS Lambda and Python
Automated the **domain creation process** using **AWS Lambda**. When a lender or **subdomain name** is specified through the UI, **Lambda** is triggered to automatically update both **private** and **public hosted zones** with the new **subdomain entries** and also integrated **Cross Account IAM Role**. Upon successful completion, **Lambda** sends a **success response** back to the UI.

### 5. Migration to Private Hosted Zones in AWS Route 53
Led the migration of all endpoints to **Private Hosted Zones** within **AWS Route 53**, enabling secure, internal communication within the **VPC**. This solution reduced **network latency** and decreased the load on the **NAT Gateway**, optimizing **resource access** and improving overall **infrastructure performance** while enhancing **security** by keeping traffic within the **VPC**.

### 6. Migration to CloudFront with App Load Balancer and NGINX
Migrated all **Angular pages** previously loaded through **CloudFront** > **App Load Balancer** > **NGINX** to enhance performance. This transition leveraged **CloudFront’s caching capabilities**, resulting in faster **page loads** and reduced **server load**, while ensuring improved **scalability** and **content delivery efficiency**.

### 7. Migration to Private API Gateways with VPC Endpoints
Migrated all **public API Gateways** and **VPC Links** to **Private API Gateways** using **VPC Endpoints**, ensuring secure and efficient communication within the **VPC**. All private gateways were linked to a **custom domain** for improved management and consistency. Additionally, the creation of **API Gateways** was automated, transitioning from **Swagger file** to **OpenAPI**, and utilizing a **CloudFormation template** with **Serverless API** for end-to-end automation of the API creation process, streamlining **deployment** and **management**.

### 8. Installation of DataDog Agent and Automation with CloudFormation
Installed **DataDog agent** on the instances. Leveraged a **CloudFormation Template** to automate the streaming of **metrics** to **Datadog**, where the **ECS service** type was configured as a **Daemon** to deploy DataDog agents, ensuring consistent and secure monitoring across all resources. Additionally, created custom **DataDog dashboards** for real-time visualization of metrics, improving **monitoring** and **alerting capabilities** for the **Production Environment**.

### 9. Automated Environment Creation and Cost Reporting Tool
Automated the creation of a complete end-to-end environment using **CloudFormation** with consistent **tagging** based on a predefined tagging document. Developed a **Python-based cost reporting tool** using **Pandas** to generate **application-wise cost reports** for each environment, enabling accurate **cost tracking** and **resource optimization**. Streamlined **resource management** and improved **financial transparency** across **development**, **staging**, and **production environments**.

### 10. Infrastructure Development with AWS Lambda, Python, API Gateway, and Jenkins
Developed an **infrastructure** using **AWS Lambda** as the backend and **API Gateway**, integrated with **Jenkins** to provide a **self-service interface** for the development team. This allowed users to **start**, **stop**, and **extend environments** independently, and using **Cross Account IAM role**, data from other accounts was accessed, eliminating reliance on the **operations team** during weekends or off-hours. The solution streamlined **environment management** and enhanced **team productivity**.

### 11. Testing Framework Upgrade and Scalable Infrastructure with ECS Fargate and AWS Lambda
Upgraded the testing framework from **Selenium 3** to **Selenium 4** and built a scalable infrastructure using **ECS Fargate** and **AWS Lambda**. This enabled the **QA team** to execute tests seamlessly with the latest features of **Selenium**. Integrated **CodePipeline** for automated deployment of individual modules, streamlining the testing process and ensuring efficient **delivery workflows**.

### 12. Centralized Email Automation with AWS Lambda and S3 Triggers for Reports Sharing
Implemented a **centralized email automation system** supporting multiple **S3 buckets** as triggers for an **AWS Lambda** function. Whenever files are uploaded to any configured bucket, the **Lambda function** automatically sends **email notifications** to the respective teams along with reports. Mailing configurations and recipient details were securely managed in **AWS Systems Manager Parameter Store**, providing a scalable and efficient solution for automated **communication workflows**.

### 13. RSYSLOG Implementation and Upgrade
**Analysis** with the team and **implementation of RSYSLOG** in the work environment. Upgraded the use of **rsyslog** from **instance metadata optional** to **required**, enhancing logging and monitoring capabilities across the infrastructure and streamed files to **s3 Bucket**.

### 14. Optimized Resource Usage with Scheduled Auto Scaling
**Optimized resource usage** by implementing **scheduled auto scaling** for **Auto Scaling Groups** based on **US holidays**. This reduced costs by scaling down resources during **non-business hours** and holidays. Additionally, **automated scaling adjustments** were made to enhance performance during **peak business hours**, ensuring efficient **resource allocation** and **cost savings**.

### 15. Automated EC2 Instance Management with AWS Maintenance Windows
**Automated** the start and stop of **standalone EC2 instances** based on **tags** using **AWS Maintenance Windows**. Implemented the solution with **CloudFormation**.

### 16. Blue-Green Deployment Automation with AWS CodePipeline and CloudFormation
Involved in automating the **blue-green deployment** process using **AWS CodePipeline** and **CloudFormation**. This setup ensured smooth deployments with **minimal downtime** by automatically switching between the blue and green environments. Additionally, implemented **artifact promotion** from lower environments to higher environments, ensuring that only **tested and validated artifacts** moved to **production**, enhancing deployment efficiency and reducing the risk of errors.

### 17. Automated CloudWatch Dashboard Creation with AWS Lambda and CloudFormation
**Automated** the creation of **CloudWatch dashboards** using **AWS Lambda** and **CloudFormation** with **custom resources**. This solution allowed for seamless and scalable dashboard creation, enabling the monitoring of key metrics across multiple **services** and **environments**, and enhancing **visibility** and **operational efficiency**.

### 18. Python Script for EC2 Performance Data Aggregation
Developed a **Python script** to retrieve and aggregate **CPU**, **memory**, and **disk metrics** of **EC2 instances** on a daily and monthly basis. This solution facilitated **capacity planning** by providing detailed **performance data**, enabling informed decisions on **resource allocation** and **scaling requirements**.

### 19. Automated AMI Creation and Management with CloudFormation, AWS Systems Manager, and Python Boto3
Using **CloudFormation**, **automated** the process of creating **AMIs** for multiple **EC2 instances** in a single operation and updated them to **Auto Scaling Groups (ASG)**. This approach replaced the manual process of taking individual AMIs and updating **launch templates (LT)** and **ASGs**. Added a **retention tag (RT)** to prevent deletion of AMIs and configured an **SCP policy** to enforce the restriction when the tag is set to **True**. Ensured that **instance tags** were propagated consistently across **AMIs**, **volumes**, and **snapshots** using **AWS Systems Manager** and **Python Boto3**. Additionally, created another infrastructure using **AWS Systems Manager** and **Python Boto3** that runs daily via **EventBridge** to automatically delete older AMIs, retaining only the latest 4 based on the **Auto Scaling Group Name tag**. This automated process **optimizes storage management** by reducing manual intervention.

### 20. DLM CloudFormation Template for AMI Lifecycle Management
Created a **DLM CloudFormation template** for managing the lifecycle of **AMIs** across multiple instances. The template used the **Name tag** to identify instances and implement a **retention policy** that ensures only the last 4 **AMIs** are kept. The solution **optimized storage management** by automating the deletion of older AMIs.

### 21. Automated CloudWatch Log Retention Management with AWS Lambda and Python
Developed an **automation solution** using **AWS Lambda** and **Python** to identify newly created **CloudWatch logs** and apply **retention policies**. The solution was deployed via an **AWS CodePipeline** for continuous integration and deployment. **EventBridge** was configured with a **custom event pattern** that monitored **CloudTrail logs** to monitor the creation of new CloudWatch logs. When new logs were detected, the Lambda function was triggered to automatically apply retention settings, ensuring that logs were retained according to organizational policies.

### 22. Automated Permission Set Creation and Deployment in AWS Organizations
**Automated** the creation and deployment of **permission sets** in **AWS Organizations** using the **Master account**. The solution involved programmatically creating permission sets and attaching them to **users** and **groups**, ensuring efficient and consistent **permission management** across the organization. To deploy these policies across multiple child accounts, **CloudFormation StackSets** were implemented. This approach enabled the **centralized and automated deployment** of resources, including the permission sets and policies, ensuring that the configuration was applied uniformly across all accounts within the organization.

### 23. Automated Bill Generation and Distribution Across Multiple Accounts
Managed **bill generation** across multiple accounts, **automated** the sharing of account bills with respective owners, and distributed **payment invoices** to the **finance team** and **CEO**, enhancing **operational efficiency** and **transparency**.








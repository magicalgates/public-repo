**1st-cron-infra-flow:**

1 - Event Bridge Rule triggers lambda based on Time zones.

2 - Lambda Scales out Autoscaling group Capacity and instance is launched.

3 - Once Instance becomes healthy System Manager Automation document is executed from Lambda.

4 - Systems Manager Automation Document contains Run Command which executes “cron-script.sh” file in the instance launched.

5 - cron-script.sh file has ruby rake command which executes jobs and few of the Workers are called and those processing happens in sidekiq servers along with Rds and Redis.

6 - Instance Metrics and Logs are streamed to CloudWatch.

**2nd-cron-infra-flow:**

1 - Event Bridge Rule triggers Cron Tz lambda based on Time zones as per 1st cron infra, from the launched instances 2nd Cron Tz lambda is triggered at particular timezones.

2 - Lambda Scales out Autoscaling group Capacity and instance is launched.

3 - Once Instance becomes healthy System Manager Automation document is executed from Lambda.

4 - Systems Manager Automation Document contains Run Command which executes “cron-script.sh” file in the instance launched.

5 - cron-script.sh file has rake command which executes jobs and processing happens along RDS and Redis.

6 - Instance Metrics and Logs are streamed to CloudWatch.

1' - We can schedule Event bridge rule for testing purpose and invoke lambda

Pipeline = To deploy code to EC2 instances.

**Note:**

- After the completion of job processing, the terminate-instance-in-auto-scaling-group SDK function is invoked to terminate the instance.
- Once the termination process is initiated in the Auto Scaling group, a 30-second lifecycle hook is managed to ensure all logs are successfully transferred to CloudWatch Logs.

**----------------------------------------------------------------------------------------------------------**

## Benefits and Cost Savings

By migrating from a traditional EC2-based cron job scheduling system to an optimized serverless solution, the following benefits and cost savings were achieved:

### **Benefits**

- **Improved Flexibility**: Scheduling became highly customizable with EventBridge, allowing precise triggers based on client requirements (e.g., specific time zones like Eastern Time).
- **Automation**: The entire process, from server scaling to cron job execution, is fully automated, reducing the need for manual intervention.
- **Enhanced Reliability**: Utilized AWS Lambda, Systems Manager, and EventBridge, which are managed services with high availability and fault tolerance.
- **Scalability**: Auto Scaling Groups ensure the infrastructure scales dynamically based on job requirements.
- **Ease of Maintenance**: Eliminated the need to manage and update EC2 instances for cron jobs manually.

### **Cost Savings**
- **Pay-as-You-Go**: Servers are only spun up when needed, significantly reducing costs associated with always-on EC2 instances.
- **Reduced Operational Costs**: The serverless architecture eliminates the overhead of maintaining and patching dedicated servers.
- **Optimized Resource Utilization**: Resources are provisioned dynamically, ensuring no idle compute power and minimal wastage.
- **Elimination of Unused Resources**: Auto-termination of instances after job completion leads to direct savings.

### **Outcome**
This migration led to a more agile, efficient, and cost-effective solution, enabling the team to focus on delivering value rather than managing infrastructure.

**-------------------------------------------------------------------------------------------------------------**

## Access to Source Code and Automation Templates

The complete source code for this project is maintained in a private repository to ensure security and proper access control. 

If you are interested in exploring the code, please contact me with your GitHub username and a brief reason for your request.

- **Email**: [yashwanths5599@gmail.com](mailto:yashwanths5599@gmail.com)
- **GitHub Issues**: Open an issue in this repository with your request.

Once verified, you will be granted access to the private repository.
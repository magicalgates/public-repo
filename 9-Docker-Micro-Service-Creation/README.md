#### ECS Service and Auto Scaling Setup Template

**Overview**  
This repository contains an **AWS CloudFormation** template to create a fully functional **ECS** setup with an **EC2 launch type**. The template provisions the following core components:  

- **ECS Cluster**  
- **Auto Scaling Group (ASG)**  
- **ECS Service**  
- **Task Definition**  
- **Target Group**  
- **ECR Repository**  
- **IAM roles, policies, and security groups**  
- **AWS CodePipeline** for deployment automation  

#### Architecture  
The template provisions the following **ECS infrastructure**:  

1. **ECS Cluster**  
   - Creates an **ECS Cluster** to manage **ECS services** on **EC2 instances**.  
2. **Auto Scaling Group (ASG)**  
   - Sets up an **Auto Scaling Group (ASG)** to scale **EC2 instances** that run **ECS tasks**.  
3. **ECS Task Definition**  
   - Defines **container settings** such as **image, memory, CPU,** and **environment variables**.  
4. **ECS Service**  
   - Manages the **desired number of tasks** to run on the **EC2 instances**.  
5. **ECR Repository**  
   - Stores **container images** in an **Amazon ECR Repository**.  
6. **Target Group**  
   - Routes traffic to **ECS tasks** via an **Application Load Balancer**.  
7. **IAM Roles and Policies**  
   - Provides **roles** for **ECS tasks** and **EC2 instances** to securely interact with **AWS services**.  
8. **Security Groups**  
   - Manages **inbound/outbound traffic** for **ECS tasks** and **EC2 instances**.  
9. **Auto Scaling Policies**  
   - Defines **scaling rules** for the **Auto Scaling Group** based on metrics like **CPU utilization**.  
10. **AWS CodePipeline**  
    - Automates the **deployment process** using **AWS CodePipeline**, which:  
      - **Source**: Pulls code from **GitHub** or **S3**.  
      - **Build**: Uses **AWS CodeBuild** to build and push the image to **ECR**.  
      - **Deploy**: Deploys the **container image** to **ECS**.  
11. **CloudWatch Logs (Optional)**  
    - Configures **CloudWatch Logs** for monitoring **ECS task activity**.  

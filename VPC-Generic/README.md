# AWS VPC Creation Template for a 3-Tier Application

## Overview

This repository contains an AWS CloudFormation template to create a generic VPC setup for a 3-tier application architecture. The template provisions the necessary networking components, including **VPC, subnets, route tables, internet gateway (IGW), NAT gateway**, and associated configurations.

## Architecture

The CloudFormation template sets up the following network infrastructure:

#### **1. VPC:**  
- A **Virtual Private Cloud (VPC)** with a customizable CIDR block.

#### **2. Subnets:**  
- **Public Subnets** (for Load Balancers and NAT Gateway)  
- **Private Application Subnets** (for application servers)  
- **Private Database Subnets** (for database instances, Redis Related)  

#### **3. Route Tables:**  
- **Public Route Table** (routes internet-bound traffic through IGW)  
- **Private Route Table** (routes outbound traffic through NAT Gateway for private subnets)  

#### **4. Internet Gateway (IGW):**  
- Allows public subnets to access the internet.

#### **5. NAT Gateway:**  
- Provides internet access for private subnets without exposing them directly.

#### **6. Security Groups (Optional):**  
- Can be defined for various application components.

## Deployment Instructions

### #### **Prerequisites**

- **AWS CLI** installed and configured with necessary permissions.
- **An AWS account** with CloudFormation access.

### #### **Steps to Deploy**

1. **Clone this repository:**
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. **Deploy the CloudFormation stack using the AWS CLI:**
   ```sh
   aws cloudformation create-change-set --change-set-name Nds-Cync-StgSqlUp-Vpc-Stack --stack-name Nds-Cync-StgSqlUp-Vpc-Stack --template-body file:///${Path}/Prefix-Vpc-Template.yml --parameters file://${Path}/Prefix-Vpc-Parameters.json --role-arn arn:aws:iam::${Account-Id}:role/Nds-Cync-StgSqlUp-Cfn-Exec-Role --tags file://${Path}/Prefix-Vpc-Tags.json --capabilities CAPABILITY_NAMED_IAM --change-set-type CREATE/UPDATE
    
   ```
3. **Wait for the stack to complete:**
   ```sh
   aws cloudformation wait stack-create-complete --stack-name MyVPCStack
   ```
4. **Verify the resources in the AWS Console under CloudFormation.**

## Outputs

Once deployed, the stack provides the following outputs:

- **VPC ID**
- **Public Subnet IDs**
- **Private Application Subnet IDs**
- **Private Database Subnet IDs**
- **Internet Gateway ID**
- **NAT Gateway ID**

## Cleanup

To delete the stack and all associated resources:

```sh
aws cloudformation delete-stack --stack-name MyVPCStack
```

## License

This project is licensed under the **MIT License**.

## Contributing

Feel free to open an issue or submit a pull request if you have improvements or additional features to propose.

## Contact

For any questions, reach out via **[email/contact details]**.


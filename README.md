<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Quebook</h1> 
    <h3>This is a social media app for O/L students in Sri lanka.</h3>
    <p>This project consists of two architectures.</p>
    <h3>1. High Level Architecture.</h3>
    <h3>2. Low Level Architecture.</h3>
    <h3>Low Level Architecture</h3>
    <a href="https://youtu.be/bLYGAvhhiGI" target="_blank">
    <img src="https://img.youtube.com/vi/bLYGAvhhiGI/hqdefault.jpg" alt="Watch the video" />
    </a>
    <p>Api of this app </p>
    <img src="https://user-images.githubusercontent.com/76420546/158219687-bb5fce0f-0157-4a77-9660-3fd8fffdeb7f.png">
    <hr>
    <img src="https://user-images.githubusercontent.com/76420546/158219718-d95d05e1-9008-41d6-9b0e-39ae017f75d7.png">
    <h3>High Level Architecture</h3>
    <p>Amazon Virtual Private Cloud (Amazon VPC)is used to launch AWS resources in a logically isolated virtual network.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookVpc.png" />
    <p>Four subnets (two public for ec2 instances and two private for database instances )are used in two avialability zones.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookSubnets.png" />
    <p>Four route tables are used to route where network traffic from subnets or gateway is directed.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookRouteTables.png" />
    <p>An internet gateway is used to connect resources in public subnets (such as EC2 instances) to connect to the internet.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookInternetGateway.png" />
    <p>Two network access control lists are used to controll inbound or outbound traffic of public and private subnets at the subnet level.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookNacls.png" />
    <p>Security groups are used to control incoming and outgoing traffic at instance level.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookSecurityGroups.png" />
    <p>Amazon Elastic Compute Clouds (Amazon EC2) are used as on-demand, scalable computing capacity to host the application in two public subnets.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookInstances.png" />
    <p>Aplication Load Balancer is used to automatically distributes incoming traffic across multiple EC2 instances in two Availability Zones.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookLoadBalancer.png" />
    <p>Target group is used to route requests from Aplication Load Balancer to EC2 instances in two Availability Zones.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookTargetGroup.png" />
    <p>Amazon EC2 Auto Scaling is used to ensure that the correct number of Amazon EC2 instances are available to handle the load for application. </p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookAutoScalingGroups.png" />
    <p>A launch template is used to specify instance configuration information and launch EC2 instances in auto sacaling Groups. </p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookLaunchTemplates.png" />
    <p>AWS CodePipeline is used as a continuous delivery service to automate the steps required to release the application.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodePipeline1.png" />
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodePipeline2.png" />
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodePipeline3.png" />
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodePipeline4.png" />
    <p>CodeDeploy is used as a deployment service to automate application deployments to Amazon EC2 instances.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodeDeploy1.png" />
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodeDeploy2.png" />
    <p>CodeDeploy is intergrated with EC2 Auto Scaling to when new Amazon EC2 instances are launched as part of an Amazon EC2 Auto Scaling group, CodeDeploy can deploy revisions to the new instances automatically.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodeDeploy3.png" />
    <p>Blue/green deployment is used as a deployment strategy to increase application availability and reduce deployment risk by simplifying the rollback process if a deployment fails.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodeDeploy4.png" />
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodeDeploy5.png" />
    <p>Parameter Store, a capability of AWS Systems Manager is used to store configuration data and secrets securely.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookParameterStore.png" />
    <p>Amazon Simple Storage Service (Amazon S3) is used to store images of application that offers industry-leading scalability, availability, security, and performance. </p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookS3.png" />
    <p>Amazon Relational Database Service (Amazon RDS) is used to set up, operate, and scale a relational database of the application in the AWS Cloud.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookRDS.png" />
    <p>* Mainly I was forcusing on backend of this app. So please check this app on a desktop or laptop computer.</p>
</body>
</html>

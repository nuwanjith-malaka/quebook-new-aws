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
    [<img src="https://img.youtube.com/vi/bLYGAvhhiGI/hqdefault.jpg" width="50%">](https://youtu.be/bLYGAvhhiGI)
    <p>This project consists of two architectures.</p>
    <h3>1. High Level Architecture.</h3>
    <h3>2. Low Level Architecture.</h3>
    <h3>High Level Architecture</h3>
    <p>Amazon Virtual Private Cloud (Amazon VPC)is used to launch AWS resources in a logically isolated virtual network.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookVpc.png" width="900px" style="border: 1px solid black;">
    <p>Four subnets (two public for ec2 instances and two private for database instances )are used in two avialability zones.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookSubnets.png" width="900px" style="border: 1px solid black;">
    <p>Four route tables are used to route where network traffic from subnets or gateway is directed.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookRouteTables.png" width="900px" style="border: 1px solid black;">
    <p>An internet gateway is used to connect resources in public subnets (such as EC2 instances) to connect to the internet.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookInternetGateway.png" width="900px" style="border: 1px solid black;">
    <p>Two network access control lists are used to controll inbound or outbound traffic of public and private subnets at the subnet level.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookNacls.png" width="900px" style="border: 1px solid black;">
    <p>Security groups are used to control incoming and outgoing traffic at instance level.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookSecurityGroups.png" width="900px" style="border: 1px solid black;">
    <p>Amazon Elastic Compute Clouds (Amazon EC2) are used as on-demand, scalable computing capacity to host the application in two public subnets.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookInstances.png" width="900px" style="border: 1px solid black;">
    <p>Aplication Load Balancer is used to automatically distributes incoming traffic across multiple EC2 instances in two Availability Zones.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookLoadBalancer.png" width="900px" style="border: 1px solid black;">
    <p>Target group is used to route requests from Aplication Load Balancer to EC2 instances in two Availability Zones.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookTargetGroup.png" width="900px" style="border: 1px solid black;">
    <p>Amazon EC2 Auto Scaling is used to ensure that the correct number of Amazon EC2 instances are available to handle the load for application. </p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookAutoScalingGroups.png" width="900px" style="border: 1px solid black;">
    <p>A launch template is used to specify instance configuration information and launch EC2 instances in auto sacaling Groups. </p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookLaunchTemplates.png" width="900px" style="border: 1px solid black;">
    <p>AWS CodePipeline is used as a continuous delivery service to automate the steps required to release the application.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodePipeline1.png" width="900px" style="border: 1px solid black;">
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodePipeline2.png" width="900px" style="border: 1px solid black;">
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodePipeline3.png" width="900px" style="border: 1px solid black;">
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodePipeline4.png" width="900px" style="border: 1px solid black;">
    <p>CodeDeploy is used as a deployment service to automate application deployments to Amazon EC2 instances.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodeDeploy1.png" width="900px" style="border: 1px solid black;">
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodeDeploy2.png" width="900px" style="border: 1px solid black;">
    <p>CodeDeploy is intergrated with EC2 Auto Scaling to when new Amazon EC2 instances are launched as part of an Amazon EC2 Auto Scaling group, CodeDeploy can deploy revisions to the new instances automatically.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodeDeploy3.png" width="900px" style="border: 1px solid black;">
    <p>Blue/green deployment is used as a deployment strategy to increase application availability and reduce deployment risk by simplifying the rollback process if a deployment fails.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodeDeploy4.png" width="900px" style="border: 1px solid black;">
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookCodeDeploy5.png" width="900px" style="border: 1px solid black;">
    <p>Parameter Store, a capability of AWS Systems Manager is used to store configuration data and secrets securely.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookParameterStore.png" width="900px" style="border: 1px solid black;">
    <p>Amazon Simple Storage Service (Amazon S3) is used to store images of application that offers industry-leading scalability, availability, security, and performance. </p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookS3.png" width="900px" style="border: 1px solid black;">
    <p>Amazon Relational Database Service (Amazon RDS) is used to set up, operate, and scale a relational database of the application in the AWS Cloud.</p>
    <img src="https://malakas3.s3.amazonaws.com/quebook/quebookRDS.png" width="900px" style="border: 1px solid black;">
    <h3>Low Level Architecture</h3>
    <p>Students can create a profile and ask questions relating to their subjects.</p> 
    <img src="https://user-images.githubusercontent.com/76420546/158170395-68ad188e-ab53-4f6e-a9f9-33f9a796ffb7.png" width="900px" style="border: 1px solid black;">
    <hr>
    <img src="https://user-images.githubusercontent.com/76420546/158170416-fc29bd08-ec9e-4df0-ae0d-20a9b83ee4ba.png" width="900px" style="border: 1px solid black;">
    <p>Asked questions can be seen in his/her profile.</p> 
    <img src="https://user-images.githubusercontent.com/76420546/158172149-f5ec097c-a847-4e6d-a369-bd4230c5419d.png" width="900px" style="border: 1px solid black;">
    <p>Student can make friends by visiting friends page.In friends page firends section will display his/her friends, suggesions section will display suggesions according to his/her school,city and grade. Find friends section will display all other registed students. Students can send friend requests, cancel requests, confirm or delete requests and unfriend students from friends page.</p> 
    <img src="https://user-images.githubusercontent.com/76420546/158174170-d6091c8d-d66b-4992-9977-030a6fdfa718.png" width="900px" style="border: 1px solid black;">
    <hr>
    <img src="https://user-images.githubusercontent.com/76420546/158174197-2911d718-4712-4d7d-b2b1-75c9b06a8572.png" width="900px" style="border: 1px solid black;">
    <p>Home page will display logged student's questions and his/her friends's questions</p>
    <img src="https://user-images.githubusercontent.com/76420546/158206657-bc3f1a49-724c-406b-bea9-bec644c073c1.png">
    <p>Latest questions page will display all questions ordered by date. Latest questions will be displayed on top.</p>
    <img src="https://user-images.githubusercontent.com/76420546/158207779-5f9db9bd-3c78-4758-a95e-2be42efe6797.png">
    <p>Subjects page will display all the subjects. Questions related to relevent subject can be seen from that subject's page.</p>
    <img src="https://user-images.githubusercontent.com/76420546/158208620-77f5ff13-1fdd-4c8d-9a5f-d57a33023a93.png">
    <hr>
    <img src="https://user-images.githubusercontent.com/76420546/158208856-52b0dcb4-3268-47da-a666-1e63b5e233b5.png">
    <p>Students can give answers,comments,upvotes and downvotes to questions. After some student viewed some question, views of that question will be incremented by one .</p>
    <img src="https://user-images.githubusercontent.com/76420546/158211740-e1babe84-337a-43c0-8c6a-b9707bc65083.png">
    <p>Students can give comments,upvotes and downvotes to answers. Question's answers will be ordered automatically according to upvotes and downvotes of that answer.Most upvoted and least downvoted answers will be shown on top.</p>
    <img src="https://user-images.githubusercontent.com/76420546/158212867-de1e113c-2c10-4f51-85d7-487877c666f5.png">
    <p>Is some student forgets his/her password he/she can reset password by entering his/her email address to send one time password reset link.</p>
    <img src="https://user-images.githubusercontent.com/76420546/158216354-53c5e935-3032-4b1c-a400-aab022802487.png">
    <hr>
    <img src="https://user-images.githubusercontent.com/76420546/158216367-ab992d82-0f7e-4518-af20-beceeda0a8d1.png">
    <p>You can see the api of this app by visiting https://murmuring-plateau-61051.herokuapp.com/api/</p>
    <img src="https://user-images.githubusercontent.com/76420546/158219687-bb5fce0f-0157-4a77-9660-3fd8fffdeb7f.png">
    <hr>
    <img src="https://user-images.githubusercontent.com/76420546/158219718-d95d05e1-9008-41d6-9b0e-39ae017f75d7.png">
    <p>* Mainly I was forcusing on backend of this app. So please check this app on a desktop or laptop computer.</p>
</body>
</html>

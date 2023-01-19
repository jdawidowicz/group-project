
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h1 align="center">TeamOne</h1>

  </a>

  <h3 align="center">Data Management Project</h3>

  <p align="center">
    Streamlined platform that will collate all the data, track sales trends and make it easier for the client to access it. 
    <br />
    <br />
    <a href="https://docs.google.com/presentation/d/1y_x_VvmxcIAlgry3qC6W5JWI1eBUgLPHkhc9J_Vx2FY/edit#slide=id.g1303be3818b_0_146">Presentation</a>
    ·
    <a href="https://docs.google.com/presentation/d/1-5-tiY3v_KmYQx5RAsCNu1ieNzIaQgGRwlOAnliCJnk/edit#slide=id.g1f71c8939ef_0_26">Demo</a>
  
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#project-background">Project Background</a>
      <a href="#built-with">Built With</a></li>
      <a href="#key-features">Key Features</a>
    <a href="#prerequisites">Prerequisites</a>
    <a href="#installation">Installation</a>
    <a href="#usage">Usage</a>
    <a href="#Further-development">Further Developments</a>
    <a href="#contact">Contact</a>
    <a href="#credits">Credits</a>
 
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Project Background

We were given a task to create a detailed database for our client. Their growing business consists of 120 cafes and their aim is to be able to track sales in an easier and more consistent way. Due to the demand the company is receiving, they need to figure out how they can best target new and returning customers, and also understand which products are selling well. Their current set up is very limited and only produces general sales reports. Our aim is to facilitate data collection and analysis for the client.


### Built With

PYTHON
<br>
Libraries (see requirements.txt for details):<br>
pandas<br>
numpy<br>
boto3<br>
psycopg2<br>
SQLAlchemy<br>

AWS
<br>
Cloudformation<br>
S3<br>
EC2<br>
Lambda<br>
Cloudwatch<br>
<br>
Grafana<br>
Docker<br>
<br>
Redshift
<br> 
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Key Features

- ETL
- Data normalization
- System and data Monitoring
- Data visualisation
- Automation
- Analytics

### Prerequisites

PYTHON 3.9 + requirements.txt
<br>
DOCKER
<br>
REDSHIFT CLUSTER
<br>

### Installation


- [ ] Clone repo
- [ ] Upload lambda_code.zip to an S3 Bucket
- [ ] Deploy the CloudFormation template, specifying the location of the deployment code in lambda_code.zip
- [ ] Put your Redshift login credentials in AWS Parameter Store
- [ ] Set up Grafana on EC2 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Extract:
<br>
CSV dropped into the intial S3 bucket triggers main Lambda to run and extracts the file for the code to process.  
<br>
<br>
Transform:
<br>
Python code normalises data using Pandas and SQL. Single file is then separated into three main tables "Orders, "Products" and "Baskets". Few temporary tabels are also used to support the process. 
<br>
<br>
Load:
<br>
Transformed data is then loaded into Redshift Warehouse.
<br>
<br>
Monitoring and Visualisation:
<br>
Cloudwatch logs and Redshift tables are available for view and analysis in Grafana. 
<br>
<br>


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
# Further developments

<br>
Next steps in improving the code are planned as follows:
<br>
- Lambda split (ET + L)
<br>
- SQS processing
<br>
- Testing
<br>
- CI/CD
<br>
- Code refactoring
<br>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

TeamOne@fakemail.co.uk
<br>
+44 555 8326 663 
<br>
teamone.co.uk
<br>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Credits

Copyright by TeamOne 2023
<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- PROJECT LOGO -->
<br />
<div align="center">
  
  <h1 align="center" style="font-size: 10px;">TeamOne</h1>

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



<br><br>
## Project Background

<br>
We were given a task to create a detailed database for our client. Their growing business consists of 120 cafes and their aim is to be able to track sales in an easier and more consistent way. Due to the demand the company is receiving, they need to figure out how they can best target new and returning customers, and also understand which products are selling well. Their current set up is very limited and only produces general sales reports. Our aim is to facilitate data collection and analysis for the client.
<br>

## Built With
<br>
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
GRAFANA<br>
Docker<br>
<br>
REDSHIFT
<br> 




<!-- GETTING STARTED -->
## Key Features
<br>
 * ETL
 * Data normalization
 * System and data Monitoring
 * Data visualisation
 * Automation
 * Analytics
<br>
<br>

## Prerequisites

<br>
Python 3.9 + requirements.txt
<br>
Docker
<br>
Redshift Cluster
<br>

## Installation
<br>

1. Clone repo
2. Upload lambda_code.zip to an S3 Bucket
3. Deploy the CloudFormation template, specifying the location of the deployment code in lambda_code.zip
4. Put your Redshift login credentials in AWS Parameter Store
5. Set up Grafana on EC2 and Docker<br>

## Usage
<br>

Extract:
<br>
CSV dropped into the intial S3 bucket triggers main Lambda to run and extracts the file for the code to process.  
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
<br><br>


## Platfrom Infrastructure
<br>
<br>
<img src="https://user-images.githubusercontent.com/95292365/213474604-a563b63a-ac36-4af9-ab1f-709be8a2df0d.png">



<!-- CONTRIBUTING -->
## Further developments

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


<!-- CONTACT -->
## Contact

TeamOne@fakemail.co.uk
<br>
+44 555 8326 663 
<br>
teamone.co.uk
<br>




<!-- ACKNOWLEDGMENTS -->
## Credits

Copyright by TeamOne 2023



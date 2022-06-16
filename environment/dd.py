from os import CLD_CONTINUED
from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB, CloudFront, Route53
from diagrams.aws.storage import S3
from diagrams.aws.database import RDS
from diagrams.generic.compute import _Compute

# Function vpc
# input {region}: str
# output ELB

def vpc(region):
    with Cluster(region):
        with Cluster("public_subnet"):
          web_server = EC2("apache_server")
          web_server2 = EC2("apache_server")
          web_server3 = EC2("apache_server")
          web_servers = [web_server, web_server2, web_server3]
        with Cluster("private_subnet"):
          app_server = EC2("php_server")
          app_server2 = EC2("php_server")
          app_servers = [app_server, app_server2]
          database_server = RDS("Mysql")
          database_replica = RDS("Mysql_replica")
        app_loadbalancer = ELB("app_elb")
        app_loadbalancer2 = ELB("app_elb")
        app_loadbalancer >> web_servers >> app_loadbalancer2 >> app_servers
        app_servers >> database_server >> database_replica
        return [app_loadbalancer, app_servers ]
with Diagram("architecture"):
    
    cloudfront = CloudFront("distribution")
    route53 = _Compute("Client") >> Route53() >> cloudfront
    vpc_one = vpc("us-east-1")
    vpc_two = vpc('london')
    cloudfront >> vpc_one[0]
    cloudfront >> vpc_two[0]
    s3 = S3("assets")
    vpc_one[1] >> s3
    vpc_two[1] >> s3
# How To Create Hadoop Cluster With Amazon EMR?

### Following are the steps to creation of hadoop cluser:

- First open aws console.

- Then click on EMR management console.

- Click on create cluster.

- Give the name of the cluster.

- Uncheck the logging box option

- Select the instance type as m4.large

- Select the number of instances.

- Select the key pair.
- Click on create cluster.

- Then once cluster created,
Click on summary and then click on master security group and add the SSH rules in inbound rule.

- Click on hardware and copy the public ip address to connect to SSH.

- Finally EMR hadoop cluster connects to SSH.

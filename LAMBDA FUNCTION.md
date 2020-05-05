# **LAMBDA FUNCTION**

* It is a serverless means you dont own server with 0 maintainence,scalability.
* For eg:-If we write the program in java or python and if we store that program or website in EC2 then to run the code we have 
to start instance we have to pay for it but LAMBDA funtion allows u to store code and it will not charge you for storage.
* The code store in LAMBDA is charged when we run the code otherwise there will be no charge to store the code.
*The charge is on CPU,RAM*TIME of running code.
<img src="images/lambda.png">

* It gives scalability and parallelization.
* For eg:-1. first code requires 1GB ram and 1 core cpu.THEN IF WE UPDATE THE CODE NOW IF
*          2. updated code requires 2GB ram and 2 core cpu.It is updated by aws i.e. scalable.
* parallelization means if you run the code and if awshas 1 million rqst to run that same code it executes that code without taking
time i.e. programmer dont want to use threading for that.

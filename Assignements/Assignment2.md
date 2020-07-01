# SQOOP(DATA INGESTION)

### STEP 1:-
- Create and EMR in aws with sqoop application.
- Connect it with ssh using mobaxterm

### STEP 2:-
- Create an RDS.
- Connect it with mysql workbench.

## EXPORTING FILE FROM HDFS TO RDBMS:-
- Unzip the Labs from link.
> 1. Download lab file in AWS EMR using below command 
>
> wget  https://dbda-labs.s3.amazonaws.com/labs.zip
>
> 2. Unzip the downloaded zip file
>
> unzip   labs.zip .
 
<img src="/Images/Epic1.png" width=800>

- Create the new directory salarydata
- Put the salarydata.txt file in the salarydata
- Check the file in salarydata directory

<img src="/Images/Epic2.png" width=800>

- Create the Database test in MYSQL workbench.
- Create table salaries2 in database test using the .sql file which is there in labs/Lab3.2 salaries2.sql\
- Run scoop command to export the salarydata.txt file in salaries2 table in MYSQL WORKBENCH.

<img src="/Images/Epic3.png" width=800>

- Check the salaries2 table in test database.
- Give command "Select * from salaries2"
- All records which is there in salarydata.txt will be inserted in salaries2 table automatically.

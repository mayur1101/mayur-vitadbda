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
 
<img src="/Images/Epic1.png" width=1000>

- Create the new directory salarydata
- Put the salarydata.txt file in the salarydata
- Check the file in salarydata directory

<img src="/Images/Epic2.png" width=1000>

- Create the Database test in MYSQL workbench.
- Create table salaries2 in database test using the .sql file which is there in labs/Lab3.2/salaries2.sql
- Run scoop command to export the salarydata.txt file which is in HDFS  to salaries2 table in MYSQL WORKBENCH.

<img src="/Images/Epic3.png" width=1000>

- Check the salaries2 table in test database.
- Run command "Select * from salaries2"
- All records which is there in salarydata.txt will be inserted in salaries2 table automatically.

## IMPORTING FILE FROM RDBMS TO HDFS.
- Create salaries table in test database by using .sql file which is there in labs/Lab3.1/salaries.sql
- Import file data in salaries table using .txt file which is there in labs/Lab3.1/salaries.txt
- Run command "SELECT * FROM SALARIES" and see the records are entered or not.
- Run scoop command to import salaries table to HDFS.

<img src="/Images/Ipic1.png" width=1000>

- Then if we want to check the file in HDFS and see the data which is stored in parts or blocks or mappers.

<img src="/Images/Ipic2.png" width=1000>

- Now if we want only salaries table salary and age column data to be stored in hdfs new directory salaries2 then run the below sccop command

<img src="/Images/Ipic3.png" width=1000>

- To See the file data which is stored in salaries2 directory.

<img src="/Images/Ipic4.png" width=3000>

- Scoop command to split the data with respect to gender column in salaries table whose salary>90000 
and import it in salraies3 directory in hdfs with 2 files one contains male records and other female records.

<img src="/Images/Ipic5.png" width=1000>

- To see the file data run the below commands

<img src="/Images/Ipic6.png" width=1000>




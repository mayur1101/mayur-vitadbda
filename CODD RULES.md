# CODD RULES

Codd rules are proposed by Dr. EDger Frank Codd.It proposed 12 rules including rule 0.

## Rule 0:-FOUNDATION RULE
This rule says that if the system claims that it is RDBMS then this system must have ability to manage there own database.

## Rule 1:-INFORMATION RULE
This rule says that every information is stored in the form of table in rows and columns otherwise it is not allowed to store in formation
in any other form.

## Rule 2:-GUARANTEED ACCESS RULE
It says that any database element should have guaranted accessible in the form of table name or primary key or column name.

## Rule 3:-SYSTEMATIC TREATMENT OF NULL VALUES
It says that in table if any information is not stored in cell then they will occupy NULL value.

## Rule 4:-ACTIVE ONLINE CATLOG
It says that the structure of database should be kept in online catalog because whoever Database administrator will be,he can check
the query of database.

## Rule 5:-THE COMPREHENSIVE DATA SUB-LANGUAGE RULE
According to rule every database should have its own language so that to make changes,manages & do transactions.And generally
every RDBMS use SQL(structured query language)

## Rule 6:-THE VIEW UPDATING RULE
It says that the new views that is created should be automatically updated by the system.

## Rule 7:-HIGH LEVEL INSERT,UPDATE AND DELETE RULE
It says that RDBMS should accessed to insert,update & delete operations and other than this intersection,union also support.

## Rule 8:-PHYSICAL DATA INDEPENDENCE
It says that any changes in physical data should not be affected on application.
for eg:-If facebook changes physical data then user should not know the affect of that.

## Rule 9:-LOGICAL DATA INDEPENDENCE
Any changes in Logical data should not affect the application level.
for eg:-If we take facebook app and if we changes the database or merge the logical database then it should not affect on end user.

## Rule 10:-INTEGRITY INDEPENDENCE
Any data inserted in table should maintain integrity i.e. if insert element in cell then it remain that only it should not change.

## Rule 11:-DISTRIBUTION INDEPENDENCE
The database used by user through application doesnot know the other user database where they are accessing from.

## Rule 12:-NON SUBVERSION RULE
RDBMS rule i.e. SQL other than that anything is not acceptable to make changes in database.

# OLAP AND OLTP:-
<img src="/Images/OLAP AND OLTP.jpg" width=600>

- From Buisness process data is send to data warehouse and vicea versa.
- The managers,analysts which are present to analyze the data which is done through data warehouse comes in OLAP and Day to Day transactions comes under OLTP.
- All the strategies are made in OLAP and we feed stratigies in OLTP buisness process.
- We have the master data transactions which are stored in data warehouse through buisness process.
- In OLAP Data Mining,Analytics and decision making takes place.
-OLTP is used for operations purposes and OLAP is used for information analyzing.

## OLAP(Online Analytical Processing)
- OLAP term was introduced by E.F. codd and it is a category of software technology that enables analysts,managers to analyze the complex data derived from the Data warehouse.

**For eg:-** If in any region there is sale going on,one product saling is very high,then the analysts will analyize the data so that he can find the sale of which product is more
and in which season on that basis the product can be stored in warehouse accordingly.
<img src="/Images/OLAP.png" width=500>

### Features of OALP:-(FASMI)
- **Fast:-** Specialized data storage for fast accessing of data.
- **Analysis:-** It lets user to enter query in interactive tool.
- **Shared:-** Multiple users can access data simultaneously.
- **MultiDimensionality:-** There are two attributes which is measure and dimension which is used for decision making.
- **Information:-** After analysis information is feasible to fed to buissness process.We depict information in the form of some Graphs and Rules.

## OLTP(Online Transaction Processing)
- It is characterized by large number of short online transactions(INSERT,UPDATE,DELETE).

**OLAP**                                                                 **OLTP**
1)OLAP standsfor online analytical process                1)OLTP stands for online transactional process.

2)OLAP operations are done on denormalized data.          2)OLTP operations are done in normalized data.

3)OLAP uses select statement to query on datawarehouse.   3)OLTP uses insert,update,delete operations frequently on db.

4)OLAP is done for buisness analytics.                    4)OLTP is done on web application.

<img src="/Images/hadoop hdfs logo.jpg" width=400>

# What is HDFS?
- Hadoop Distributed File System(HDFS) is the world’s most reliable storage system. It is best known for its fault tolerance and high availability.
- HDFS is designed to store and manage a huge volume of data in the efficient manner.

<img src="/Images/hdfs.png" width=400>

- Normal traditional systems has default blocksize of 4-6kb and HDFS default blocksize is 128MB and of Apache default blocksize is 75 MB.

- FORMULA FOR CALCULATING THE TOTAL BLOCKS OF FILE.
- Total no. of blocks=File size/block size
- Replication factor is made for the failure.The default replication factor is 3 and it can be configurable.
- So the total number of boxes will be:-
Total no. of blocks=File blocks*Replication factor.

## Advantages of HDFS:-
- HDFS can be implemented on community hardware.
- HDFS is designed for large size files which is in TB/GB.
- HDFS is suitable for streaming data access i.e. It has written once but can read multiple times.for eg:-Log files.
- When system Failure then the automatic recovery of the system is done by HDFS.

## Disadvantages of HDFS:-
- HDFS is not suitable for files which is in small size.
- HDFS is not suitable to read from a random position within the file.It can read either from start or from end.
- HDFS does not support the multiple writing to the files from multiple writters.

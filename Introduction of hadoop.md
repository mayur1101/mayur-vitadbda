# Introduction to hadoop
<img src="Images/hadoop logo.png" width=200>

->It is a apache based open source framework.

->It is implemented in java.

->It has a distributed storage i.e. we can store data in multiple nodes in cluster and it is done by HDFS(hadoop distributed file system).

->It has a distributed processing and it is accomplished by mapreduce.

->In hadoop simple programming model is maintained.

->It supports parallel processing for fast processing.

->Is has local compuation and storage.

# Brief history of hadoop
History of Hadoop had started in the year 2002 with the project Apache Nutch. Hadoop was created by Doug Cutting, the creator of Apache Lucene, the widely used text search library. Hadoop has its origins in Apache Nutch, an open source web search engine which itself is a part of Lucene Project.

#### 2002 – 2004
Apache Nutch was started in the year 2002 by Doug Cutting which is an effort to build an open source web search engine based on Lucene and Java for the search and index component. Nutch was based on sort/merge processing. In June 2003, it was successfully demonstrated on 4 nodes by crawling 100 million pages. However they realised that their architecture wouldn’t scale to billions of pages on web. There comes the help with the publication of a paper in 2003 that described the architecture of the Google’s Distributed Filesystem, called GFS which has been used in production at Google which would solve their storage needs for the very large files generated as part of the web crawling and indexing process.

#### 2004 – 2006
In the year 2004, they started writing the open source implementation called Nutch Distributed Filesystem (NDFS). In the same year Google published a paper that introduces MapReduce to the world. Early in the year 2005, the Nutch developers had a working MapReduce Implementation in Nutch and by the middle of that year all the major Nutch algorithms had been ported using the MapReduce and NDFS (Nutch Distributed FileSystem). In Febraury, 2006 they moved out of Nutch to form an independent subproject of Lucene called Hadoop.

2004 : Initial versions of  what is now Hadoop Distributed FileSystem and MapReduce implemented by Doug Cutting and Mike Cafarella.
December 2005 : Nutch ported to a new framework. Hadoop runs reliably on 20 nodes.

#### 2006 – 2008
Doug Cutting joined Yahoo! in the year 2006, which provided him the dedicated team and resources to turn Hadoop in to a system that ran at web scale. Hadoop was made Apache’s top level project in the year 2008.

February 2006 : Apache Hadoop project officially started to support the standalone development of MapReduce and HDFS.

February 2006 : Adoption of Hadoop by Yahoo! Grid Team.

April 2006 : Sort benchmark ( 10 GB/node ) run on 188 nodes in 47.9.

May 2006 : Yahoo! set up a Hadoop 300 nodes research cluster.

May 2006 : Sort benchmark run on 500 nodes in 42 hours ( better hardware than April benchmark )

October 2006 : Research cluster reaches 600 nodes.

December 2006 : Sort benchmark run on 20 nodes in 1.8 hours, 100 nodes in 3.3 hours, 500 nodes in 5.2 hours, 900 nodes in 7.8 hours.

January 2007 : Research cluster reaches 900 nodes.

April 2007 : Research clusters – two cluster of 1000 nodes.

April 2008 : Won 1 Terabyte sort benchmark in 208 seconds on 990 nodes.

October 2008 : Loading 10 Terabytes of data per day into research clusters.

#### 2008 – now
After 2008 there is a full time development that is going on. There are many releases of Hadoop, you can find them here.

March 2009 : 17 clusters with a total of 24,000 nodes.

April 2009 : Won the minute sort by sorting 500 GB in 59 seconds on 1,400 nodes and 100 TB sort in 173 minutes on 3,400 nodes.

2011 : Yahoo was running its search engine across 42,000 nodes.

July 2013 : Gray sort by sorting at a rate of 1.42 Terabytes per minute.

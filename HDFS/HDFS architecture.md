# **HDFS ARCHITECTURE**
<img src="/Images/hdfs architecture.jpg" width=600>
- Hadoop Distributed File System follows the master-slave architecture. Each cluster comprises a single master node and multiple slave nodes.
- Internally the files get divided into one or more blocks, and each block is stored on different slave machines depending on the replication factor.
- The master node stores and manages the file system namespace, that is information about blocks of files like block locations, permissions, etc.
- The slave nodes store data blocks of files.
- The Master node is the NameNode and DataNodes are the slave nodes.

## HDFS NAMENODE
- NameNode is the centerpiece of the Hadoop Distributed File System. It maintains and manages the file system namespace and provides the right access permission to the clients.
- The NameNode stores information about blocks locations, permissions, etc. on the local disk in the form of two files:
   - **Fsimage:** Fsimage stands for File System image. It contains the complete namespace of the Hadoop file system since the NameNode creation.
   - **Edit log:** It contains all the recent changes performed to the file system namespace to the most recent Fsimage.

#### Functions of HDFS NameNode
- It executes the file system namespace operations like opening, renaming, and closing files and directories.
- NameNode manages and maintains the DataNodes.
- It determines the mapping of blocks of a file to DataNodes.
- NameNode records each change made to the file system namespace.
- It keeps the locations of each block of a file.
- NameNode takes care of the replication factor of all the blocks.
- NameNode receives heartbeat and block reports from all DataNodes that ensure DataNode is alive.
- If the DataNode fails, the NameNode chooses new DataNodes for new replicas.

Before Hadoop2, NameNode was the single point of failure.
The High Availability Hadoop cluster architecture introduced in Hadoop 2, allows for two or more NameNodes running in the cluster in a hot standby configuration.

## HDFS DATANODE
DataNodes are the slave nodes in Hadoop HDFS. DataNodes are inexpensive commodity hardware. They store blocks of a file.

#### Functions of HDFS Datanode
- DataNode is responsible for serving the client read/write requests.
- Based on the instruction from the NameNode, DataNodes performs block creation, replication, and deletion.
- DataNodes send a heartbeat to NameNode to report the health of HDFS.
- DataNodes also sends block reports to NameNode to report the list of blocks it contains.

## Secondary NameNode
<img src="/Images/secondary namenode.png" width=500>

- Apart from DataNode and NameNode, there is another daemon called the secondary NameNode.
Secondary NameNode works as a helper node to primary NameNode but doesn’t replace primary NameNode.
- When the NameNode starts, the NameNode merges the Fsimage and edit logs file to restore the current file system namespace. 
- Since the NameNode runs continuously for a long time without any restart, the size of edit logs becomes too large. This will result in a long restart time for NameNode.
- Secondary NameNode solves this issue.Secondary NameNode downloads the Fsimage file and edit logs file from NameNode.
- It periodically applies edit logs to Fsimage and refreshes the edit logs. 
The updated Fsimage is then sent to the NameNode so that NameNode doesn’t have to re-apply the edit log records during its restart. 
- This keeps the edit log size small and reduces the NameNode restart time.
- If the NameNode fails, the last save Fsimage on the secondary NameNode can be used to recover file system metadata.
The secondary NameNode performs regular checkpoints in HDFS.

## CheckPoint NameNode
- The Checkpoint node is a node that periodically creates checkpoints of the namespace.
- Checkpoint Node in Hadoop first downloads Fsimage and edits from the Active Namenode. 
Then it merges them (Fsimage and edits) locally, and at last, it uploads the new image back to the active NameNode.
- It stores the latest checkpoint in a directory that has the same structure as the Namenode’s directory.
This permits the checkpointed image to be always available for reading by the NameNode if necessary.

## Backup Node
- A Backup node provides the same checkpointing functionality as the Checkpoint node.
- In Hadoop, Backup node keeps an in-memory, up-to-date copy of the file system namespace. It is always synchronized with the active NameNode state.
- It is not required for the backup node in HDFS architecture to download Fsimage and edits files from the active NameNode to create a checkpoint. 
It already has an up-to-date state of the namespace state in memory.
- The Backup node checkpoint process is more efficient as it only needs to save the namespace into the local Fsimage file and reset edits.
NameNode supports one Backup node at a time.

## Blocks in HDFS
<img src="/Images/blocks hdfs.png" width=500>

- Internally, HDFS split the file into block-sized chunks called a block. The size of the block is 128 Mb by default. One can configure the block size as per the requirement.

## Replication Management
- For a distributed system, the data must be redundant to multiple places so that if one machine fails, the data is accessible from other machines.
- In Hadoop, HDFS stores replicas of a block on multiple DataNodes based on the replication factor.
- The replication factor is the number of copies to be created for blocks of a file in HDFS architecture.
- If the replication factor is 3, then three copies of a block get stored on different DataNodes.
So if one DataNode containing the data block fails, then the block is accessible from the other DataNode containing a replica of the block.
- If we are storing a file of 128 Mb and the replication factor is 3, then (3*128=384) 384 Mb of disk space is occupied for a file as three copies of a block get stored.
- This replication mechanism makes HDFS fault-tolerant.

## Rack in HDFS
- Rack is the collection of around 40-50 machines (DataNodes) connected using the same network switch. If the network goes down, the whole rack will be unavailable.
- To ensure that all the replicas of a block are not stored on the same rack or a single rack, 
NameNode follows a rack awareness algorithm to store replicas and provide latency and fault tolerance.
- Suppose if the replication factor is 3, then according to the rack awareness algorithm:
   - The first replica will get stored on the local rack.
   - The second replica will get stored on the other DataNode in the same rack.
   - The third replica will get stored on a different rack. 

## HDFS READ AND WRITE OPERATION
**1)Write Opeartion**
- When a client wants to write a file to HDFS, it communicates to the NameNode for metadata.
The Namenode responds with a number of blocks, their location, replicas, and other details.
Based on information from NameNode, the client directly interacts with the DataNode.
-The client first sends block A to DataNode 1 along with the IP of the other two DataNodes where replicas will be stored.
When Datanode 1 receives block A from the client, DataNode 1 copies the same block to DataNode 2 of the same rack. 
As both the DataNodes are in the same rack, so block transfer via rack switch. 
Now DataNode 2 copies the same block to DataNode 4 on a different rack. As both the DataNoNes are in different racks, so block transfer via an out-of-rack switch.
- When DataNode receives the blocks from the client, it sends write confirmation to Namenode.
- The same process is repeated for each block of the file.

**2)Read Operation**
- To read from HDFS, the client first communicates with the NameNode for metadata. 
The Namenode responds with the locations of DataNodes containing blocks. After receiving the DataNodes locations, the client then directly interacts with the DataNodes.
- The client starts reading data parallelly from the DataNodes based on the information received from the NameNode. The data will flow directly from the DataNode to the client.
- When a client or application receives all the blocks of the file, it combines these blocks into the form of an original file.

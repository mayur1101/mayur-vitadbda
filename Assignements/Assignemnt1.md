# HDFS COMMANDS USING AWS EMR

### Step 1:-
create the aws emr hadoop cluster.

### step 2:-
**Download lab file in AWS EMR.**

<img src="/Images/pic1.png" width=500>

### step 3:-
**Unzip the downloaded zip file.**

<img src="/Images/pic2.png" width=500>

## 1)View the hdfs dfs Command

<img src="/Images/pic3.png" width=500>

## 2) Create a Directory in HDFS
**a.Enter the following -ls command to view the contents of the user’s root directory  in HDFS, which is /user/root.**

You do not have any files in /user/root yet, so no output is displayed.  Run the -ls command again, but this time specify the root HDFS folder:  

<img src="/Images/pic4.png" width=500>

Notice how adding the / in the -ls command caused the contents of the root  folder to display, but leaving off the / showed the contents of /user/root, which  is the default prefix if you leave off the leading / on any of the hadoop commands  (assuming the command is run by the “root” user).  

**b.Enter the following command to create a directory named mayur_test in HDFS:**

**c.Verify that the folder was created successfully:** 

<img src="/Images/pic5.png" width=500>

**d.Create a couple of subdirectories for test:** 
Notice how the -p command can be used to create multiple directories. The  second command above will fail if you omit the -p.   

**e.Use the -ls command to view the contents of /user/root:** 
Notice you only see the test directory. To recursively view the contents of a folder,  use -ls -R: 

<img src="/Images/pic6.png" width=500>

<img src="/Images/pic7.png" width=500>

## 3) Delete a Directory  
**a. Delete the test2 folder (and recursively, its subcontents) using the -rm -R  command:**

<img src="/Images/pic8.png" width=500>

**b. Now run the -ls -R command:**  

<img src="/Images/pic9.png" width=500>

Note:-Notice Hadoop created a .Trash folder for the root user and moved the deleted  content there. 
The .Trash folder empties automatically after a configured amount  of time.  

## 4) Upload a File to HDFS  
**a. Now let’s put a file into the test folder. Change directories to  /root/devph/labs/Lab2.1:**

**b. Notice this folder contains a file named data.txt:**

**c.Run the following -put command to copy data.txt into the test folder in HDFS:**

**d.Verify that the file is in HDFS by listing the contents of test:**

<img src="/Images/pic10.png" width=500>

## 5) Copy a File in HDFS  
**a. Now copy the data.txt file in test to another folder in HDFS using the -cp  command:**

**b. Verify that the file is in both places by using the -ls -R command on test. The  output should look like the following:**

**c. Now delete the data2.txt file using the -rm command:**

<img src="/Images/pic11.png" width=700>

## 6) View the Contents of a File in HDFS  
**a.  You can use the -cat command to view text files in HDFS. Enter the following  command to view the contents of data.txt:**

<img src="/Images/pic12.png" width=700>

**b. You can also use the ‐tail command to view the end of a file:**

<img src="/Images/pic13.png" width=700>

Notice the output this time is only the last 20 rows of data.txt.  

## 7 ) Getting a File from HDFS  
**a. See if you can figure out how to use the get command to copy test/data.txt from  HDFS into your local /tmp folder.**

<img src="/Images/pic14.png" width=500>

## 8 ) The getmerge Command  
**a. Put the file /root/devph/labs/demos/small_blocks.txt into the test folder in  HDFS. You should now have two files in test: data.txt and small_blocks.txt.**

<img src="/Images/pic15.png" width=500>

**Run the following getmerge command:**

<img src="/Images/pic16.png" width=500>

**c. What did the previous command do? Did you open the file merged.txt to see what  happened?**
Answer: The two files that were in the test folder in HDFS were merged into a  single file and stored on the local file system.  

## 9 ) Specify the Block Size and Replication Factor  
**a. Put /root/devph/labs/Lab2.1/data.txt into /user/root in HDFS, giving it a  blocksize of 1,048,576 bytes.**
Hint:-The blocksize is defined using the dfs.blocksize property on the command line.  

**b. Run the following fsck command on data.txt:**  

**c. How many blocks are there for this file?**
Answer: The file should be broken down into two blocks. 

<img src="/Images/pic17.png" width=800>












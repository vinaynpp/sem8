# DC

* MCQ
  * Module 4
    * Which of the following is not a category of load balancing algorithm.
      * Static
      * Deterministic
      * Distributed
      * **Decentralized**
    * Load-balancing approach is used -------
      * Tasks are scheduled to improve performance  
      * **Tasks are distributed among nodes so as to equalize the workload of nodes of the system**
      * Simply attempts to avoid idle nodes while processes wait for being processed
      * Minimization of IPC costs
    * Remote processes are given higher priority than local processes is known as
      * Selfish
      * Intermediate
      * **Altruistic**
      * Controlled
    * Location policy in sender initiated process migration uses ------ variations
      * 2
      * **3**
      * 4
      * 5
    * In ------------- method a node broadcast a State-Information-Request message when its state switches from normal to either under loaded or overloaded region
      * Exchange by polling
      * **On-demand exchange**
      * Periodic broadcast
      * Broadcast when state changes
    * In __________ load balancing algorithms entities act as autonomous ones and make scheduling decisions independently from other entities
      * Cooperative
      * **Noncooperative**
      * Synchronous operated
      * All  
    * Following is NOT Issue in Designing Load Balancing Algorithms
      * State Information Exchange Policy
      * Location Policy
      * Load Estimation Policy
      * **No A priori Knowledge about the processes**
    * To improve performance ----- approach is used
      * **Task assignment**
      * Load Estimation  
      * Load balancing
      * Load sharing
    * Tasks are distributed among nodes so as ------- the workload of nodes of the system in load balancing approach
      * **to equalize**
      * to prioritize
      * to complete
      * to fulfill
    * Tasks are distributed among nodes so as to equalize  the workload of nodes of the system-------- approach is used
      * Task assignment  
      * Load Estimation  
      * **Load balancing**
      * Load sharing
    * Simply attempts to avoid ----- nodes while processes wait for being processed in load sharing approach
      * heavy
      * overloaded
      * light loaded
      * **idle**
    * Simply attempts to avoid idle nodes while processes wait for being processed ------ approach is used
      * Task assignment  
      * Load Estimation  
      * Load balancing
      * **Load sharing**
    * To avoid poor scalability coming from broadcast messages the partner node is searched by polling the other nodes on by one, until poll limit is reached is known as--------
      * **Exchange by polling**
      * On-demand exchange
      * Periodic broadcast
      * Broadcast when state changes
  * Module 5
    * Updating a website with an editor, if you want to view your updated website, you have to refresh it, otherwise the browser uses the old cached website content , Is example of__________
      * Monotonic Reads
      * Monotonic Writes
      * **Read Your Writes**
      * Writes Follow Reads
    * Which of the following is client centric consistency model
      * Strict consistency
      * Linear consistency
      * Sequential consistency
      * **Read Your Writes**
    * Distributed e-mail database with distributed and replicated user-mailboxes, Is example of __________
      * **Monotonic Reads**
      * Monotonic Writes
      * Read Your Writes
      * Writes Follow Reads
    * Writes done by a single process are seen by all other processes in the order in which they were issued, but writes from different processes may be seen in a different order by different processes.
      * **FIFO Consistency**
      * Causal Consistency
      * Sequential Consistency
      * Weak Consistency
    * _______consistency provides consistency gurantees for a single client with respect to the data stored by that client
      * Data-centric
      * **Client centric**
      * Eventual
      * Entry
    * ___________ is a set of technologies for copying and distributing data and database objects from one database to another.
      * **Replication**
      * Database Mirroring
      * Log Shipping
      * Consistency
    * _______is a property to consider in faulty distributed environments
      * Replication
      * **recovery**
      * concurrency
      * Consistency
    * Fault tolerance is a ______ requirement that requires a system to continue to operate,even in the presence of faults
      * **Non-functional**
      * Functional
      * Concurrent
      * Redundant
    * In Distributed system, _____ can be hidden
      * **Replication**
      * Fault tolerance
      * concurrency
      * Consistency
    * ________consistency is fine if clients always access the same replica.
      * Data-centric
      * Client centric
      * **Eventual**
      * Entry
    * In client-Initiated Replicas if there is return data from cache, it is termed as ------
      * **Cache hit**
      * Cache miss
      * Cache place
      * Cache loss
    * Select which is not a type of replica
      * Client-Initiated Replicas
      * Server-Initiated Replicas
      * Permanent Replicas
      * **object initiated replica**
    * The --------are dynamically created at the request of the owner of the Distributed System
      * Client-Initiated Replicas
      * **Server-Initiated Replicas**
      * Permanent Replicas
      * object initiated replica
    * The --------are initial set of replicas and  Other replicas can be created from them
      * Client-Initiated Replicas
      * Server-Initiated Replicas
      * **Permanent Replicas**
      * object initiated replica
    * The---------are caches and have temporary storage
      * **Client-Initiated Replicas**
      * Server-Initiated Replicas
      * Permanent Replicas
      * object initiated replica
    *
  * Module 6
    * What are characteristics of distributed file system ?
      * **Its users, servers and storage devices are dispersed**
      * Service activity is not carried out across the network
      * They have single centralized data repository
      * There are multiple dependent storage devices
    * What are not the characteristics of a DFS ?
      * login transparency and access transparency
      * Files need not contain information about their physical location
      * **No Multiplicity of users**
      * No Multiplicity if files
    * What are the advantages of file replication ?
      * **Improves availability &performance**
      * Decreases performance
      * They are consistent
      * Improves speed
    * The file once created can not be changed is called ________
      * **immutable file**
        * mutex file
        * mutable file
        * Mutual exclusive file
    * _______ is not possible in distributed file system
      * File replication
      * **Migration**
      * Client interface
      * Remote access
    * Which one of the following hides the location where in the network the file is stored?
      * **transparent distributed file system**
      * hidden distributed file system
        * escaped distribution file system
      * spy distributed file system
    * In distributed file system, a file is uniquely identified by _________________
      * host name
        * local name
      * **the combination of host name and local name**
      * Priority number
    * The NFS client and server modules communicate using ...................................
      * **remote procedure call**
      * Function
      * Interrupt
      * RMI
    * The automounter maintains a table of....................... with a reference to one or more NFS servers listed against each.
      * remote procedure call
      * mount protocol
      * **Pathnames**
      * Lookup
    * The-------------- operation looks for a single part of a pathname in a given directory and returns the corresponding file handle and file attributes.
      * svmlink
      * rmdir
      * Readlink
      * **Lookup**
    * The NFS client module caches the results of ------------------- operations in order to reduce the number of requests transmitted to servers.
      * svmlink,rmdir, read and write
      * rmdir,read,lookup and write
      * **read, write, getattr, lookup and readdir**
      * Lookup, getattr, readdir, and rmdir
    * AFS has two unusual design characteristics:
      * Reliability, Scalability
      * **Whole-file serving, Whole-file caching**
      * file serving, file catching
      * security, file catching
    * The name space of AFS seen by user processes is a conventional UNIX directory hierarchy, with a specific subtree ----------- containing all of the shared files.
      * **cmu**
      * tmp
      * root
      * lib
    * AFS is implemented as two software components that exist as UNIX processes called -------- and -------
      * **Vice and Venus**
      * tmp and root
      * Vice and Lib
      * lib and venus
    * A flat file service is implemented by the -------�
      * Venus
      * lib
      * **Vice servers**
      * Venus processes
    * The ------- provides a mapping between text names forfiles and their UFIDs.
      * object service
      * file service
      * **directory service**
      * thread service
    * A------- runs in each client computer, integrating andextending the operations of the flat file service and the directory service
      * **client module**
      * file module
      * service module
      * server module
    * The X.500 name tree is called the ------------
      * **Directory Information Tree (DIT)**
      * Directory Retrieval Tree (DRT)
      * Directory Traversal Tree (DTT)
      * Directory Searching Tree (DST)

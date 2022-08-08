Linux networking and Troubleshooting 
- mac address : unique fingerprint of the network interface -
- IP address : Uique address on the network 
- Subnet : Seperates the IP into network and host addresses
- Gateway : The connection leads outside of the local network
- DNS Host :  Translates hostname into IP address
- DNS Domain : The lookup domain for the host 

# HTTP
# SSL
# DNS 
# TCP
# UDP
# ICMP
# WebSocket

# CI Pipeline 
- build, unit test, integration testing 

# CD pipeline
- Deploy, Staging, pre-prod, prod, monitor

# diffrence between Process and Thread?


* How to generate ssh key? 

# Connecting to Git/BB/AWS CLI

* Github 


* Locating network informaiton and store in text file 
IP address, netmask, gateway, DNS nameserver, and domain 
$ touch network.txt  ---> file to store network info
$ systemctl status NetworkManager  --> to check if network manager is runnning 
$ nmcli c show
$ nmcli d show ens5

* Network Topology 
- Switches: forwards packets within the internal network 
- Routers: forwards packets between networks
- Data travels through both to reach a destination outside of the LAN (payload+destination address+return address+address of network card + GW card address)
- Cloud network is software define simulation of traditional network ( enable granual level accesibility)

* OSI Model 
- Application : interface (HTTP)
                -   Troubleshoot : varify app funciton and DNS
- Presentationo : Converts request from app into universal format (SSL)
- Session : Permists the ability to open close and manage a session between the proces and response (SSL)
- Transport : define how data will be sent? Proving validation and security (TCP/UDP)
                -   Troubleshoot : Verify blocked or damaged ports, firewalls, QoS
- Network : Best path to reach destination (IP)
                -   Troubleshoot : Verify address routing configuration, bandwidth, authentication 
- Data link : communicaiton between adjacent modes [MAC] (Ethernet)
                -   Troubleshoot : Verify switch, VLAN config, mac addr, IP conflicts
- Physical : Bit level transmission (ethernet physical, infrared)
                -   Troubleshoot : Verify physical components

IPv4 Classes (32 bit address)
Class A - 0    0.0.0.0 to 127.255.255.255
Class B - 10   128.0.0.0 to 191.255.255.255
Class C - 110  192.0.0.0 to 223.255.255.255
Class D - 1110 224.0.0.0 to 239.255.255.255  # reserved for multicast
Class E - 1111 240.0.0.0 to 255.255.255.255  # reserved for experimental use

* ARP (Address Resolution Protocol) ~ use for LAN connections 
-  ARP table, APR is necessary to map layer3 (IP) addressing to Layer2 (MAC) addressing 

$ nmcli d show | grep 192 
$ ip n    ~ APR table is dynamically updated and can be viewed using the ip n command 


* DNS (Domain Name Service)
- DNS is layer 7 communication protocol user to discover IP addr with given domain 
- step 1: Root server .
- srep 2: TLD (Top Level Domain) server resolves the .com; root server answer domain queries recarding TLD 
- step 3: Name serverresolve the domain portion of the query, example.com

$ dig -4 www.google.com
$ dig -4 www.google.com +trace | awk 'lenght($0)<50'


* TCP (Transmission Control Protocol) 3-way-Handshake
- Hight reliable connection protocol, Positive ack with retransmission (PAR)
- Data is retransmited with acknowledgeement isn't received 
- the layer 4 data is refer to segments, each segment contains a checksum for verificaiton upon receipt

 Host A             Host B
 1. Syn req sent from A to B
 2. Syn-Ack is sent from B to A
 3. Ack + Data from A to B

* Packet Connection sequesnce 
1. DNS: if domain being used, DNS query will be sent to get the IP address 
2. ARP: An ARP request is sent id internal network devices need MAC addresses as part of this connection 
3. TCP: TCP 3-way handshake will initiate SYN -> SYN ACK -> ACK
4. Connection: Connection data will be passed back and forth between src and destination

* Creating SSH Tunnel 

Client1 cannot connet directly with Server2 due to firewall settings. Will need to construct SSH tunnel through Server1 to view content on Server2

# System Design:
* Requirements
    1. Functional requirements 
    2. Technical requirements - Reliable (fault tolerant), Scalable, Maintainability and cost effective. 
    3. Trade-off
* API

* Back-end

* Cache 
 - Cache-Policies (to store most relevent information) using LRU (list recently use) policy and LFU (list frequently use policy)
 - Benifits of cache 
    - reduce network load 
    - faster data
    - reduce load on database


* CDN

* Client 

* CMS

* Cookie

* Database/DBMS
- Relational Database : Structured Query Language (SQL) is the standard and most widely used programming language for relational databases. It is used to manage and organize data in all sorts of systems in which various data relationships exist.
- NoSql Database : document db, Key Value store, column-oriented db, Graph db, MongoBD, DynamoDB
                    - increase the speed, reliability and scalability of your database solutions
- In-Memory DB : Memcached, Redis, Aerospike, Tarantool

* Sharding DB (with master slave config)
- Pros
    - MemCached DB
    - fast speed 
- cons
    - Joins across shards 

* DNS

* Front-end

* latency

* Load Balance

* Mobile Web / Native

* NoSql

* Refactor

* REST/Restful 
Get - Read 
Put - write to server as update to exsisting line/resource on server
Post - write to server with new line/resource on the server,
     - more than one post by user will create multiple resources on the server
Delete - write to server to delete exsisting line/resource on server

* Server

* Sharding -  Sharding is a method for distributing a single dataset across multiple databases, which can then be stored on multiple machines. This allows for larger datasets to be split in smaller chunks and stored in multiple data nodes, increasing the total storage capacity of the system.



# cloud data migration (example)
* Gather requirements 
- data range from 300 TB to 10 TB (hugh data spread onto geo regions)
- transport data securly in shortest time frame 
- Need technical skills 
- Corporate VPN connecting all the sites should be avaible 
- data migration to be performed during business hours 
Challenge --- big size of data around 300 TB 

- Snowball will move data from DC to cloud -- to move terabyte, petabyte of data will be dump on the snowball (Secure with own key and data will be encrypted) 
- S3 transfer acceleration ( bandwidth required was not sufficient )
- Kinesis Firehose (IOT device data ) ( not sreamable data)
- Storage Gateway 
- ISV connector ( third part tool)
- Direct Connect 
- VPN connection (BW will be constrain with 300 TB of data)

Cloud Migration Best Practices 
* Migration basics 
* top 10 Best Practices
* The right tool for the job
* Planning your migration 
* Transferring data 

Migration Drivers: Agility/DEv PRoductivity, data center consolidation, Acquisitions or Diverstitures, Large-scale Compute Intensive Workloads, Digital Transformation, Facility or Real Estate Decisions, Cost Reduction, Colocation or outsourcing contract changes 


Cloud computing contraints 
- data governanace, regulatory compliance, Security, Licensing
- Sutability of application --> Monolithic apps and appps with device dependency are diffcult to migrate ot cloud env 
- Need for advance tooling --> patching, version control, automated deployments and cloud orchestration my be new requirement for ops team 
- Financial Implecation --> before the assets of existing on-prem data centers are fully depreciated, the addition of pay-per-use cloud costs results in double expenses 

* Six R's of cloud Migration 
- Rehosting (lift and Shift) --> with legacy app, sometime it makes the most sense to simply rehost the existing app in cloud infra
- Replatforming (life, Thinker and Shift) In some cases, minor changes to app architectures may be necessary in order to move them to cloud 
- Repurchesing If app feature decay or other logistics (such as cost) makes migration problematic. 
- Refactoring/Rearchitecting --> Plan -> Code -> Test -> Build
- Retire
- Retain

The agile Backlog:
- Prioritization: level of effort, business values, dependency, Rishk Management 
- Phased approach: Agile iterations, Feedback loops, Demonstrate progress
- Collaboration: cross-functional
 Agile review
 Agile retrospective

# Data transport 
No. of days = (total bytes) / (megabuts per sec * 125 * 100 * network utilization * 60 sec * 60 min * 24 hours)
- Direct connect 
- Pthysical data transport 
- Cloud Storage Gateways  

# AWS SA 
* IAM 
- users 
- Groups 
- Roles
- Policies 

* S3 ( s3 is universal namespace, ei. name must be unique globally.)
- S3 standerd 
    - 99.99% avaibility, 99.11'9% durability, 
    - stored redundantly accross multiple devices in multiple facilities and is designed to sustain the loss of 2 facilities concurrently. 

- S3 - IA (infrequent access)
    - Fo data this is accessed less frequently, but requires rapid access when needed.
    - lower fee than s3, but you are changes a retrival fee. 

- S3 One Zone - IA 
    - When you want a lower-cost option for infrequent accessed data, but do not require the multiple avaibility zone data resilince. 

- S3 - Intelligent Tiering 
    - designed to optimize costs by automatically moving data to most cost-effective access tier, without performance impact or oprations overhead. 

- S3 Glacier
    - S3 Glacier is a secure, durable, and low-cost storage class for data archiving. 
    - Retrival times configurable from minutes to hours. 

- S3 Glacier Deep archive
    - It is AWS s3 lowest-cost storage class where a retrival time of 12 hours is acceptable. 

- Querying S3 with Athena and Macie
    - Athena 
        - allows to query S3 with SQL and athena is serverless application 
        - Commonly used to analyse log data stored in s3
    - Macie 
        - is use to find PII (personal identifyable info in S3) with help of ML and Natural language (Natural language processing (NLP) refers to the branch of computer science—and more specifically, the branch of artificial intelligence or AI—concerned with giving computers the ability to understand text and spoken words in much the same way human beings can.)
        - CAn be used to analyse CloudTrail Logs for suspicious API activity 
        - Includes Dashboards, Reporting and Alerting 
        - Great for PCI-DSS compliance nad preventing ID theft 


* S3 Transfer Acceleration 
- S3 transfer acceleration untilises the cloudfront edge network to accelerate your uploads to the s3
- Instead of uploding directly to your s3 bucket, you can use a distinct URL to upload directly to an edge location whihc will then transfer that file to s3. you wil get distinct URL to upload to .. 

* CloudFront ~ Content Delivery Network (CDN) 
- A system of distributed servers (networks) that deliver wabpages and other web content to a user based on the geographic locations of the user, the origin of the webpage and content delivery server. 

* EC2
* 

# Encryption 
* end to end encryption 
* 



    

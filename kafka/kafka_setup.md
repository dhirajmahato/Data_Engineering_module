## Apache Kafka ?
is a distributed event store & stream processing platform

Producer  ----> Kafka Cluster  --> Consusmer

Setups config on AWS EC2
- Install Java on client
- ```
    sudo yum install java-1.8.0
    java -version

    wget https://dlcdn.apache.org/kafka/3.5.0/kafka_2.13-3.5.0.tgz
    tar -xzf kafka_2.13-3.5.0.tgz
  ```
 Start Zoo-keeper:
-------------------------------
```
bin/zookeeper-server-start.sh config/zookeeper.properties
```
Open another window to start kafka
But first ssh to to your ec2 machine as done above


Start Kafka-server:
----------------------------------------
Duplicate the session & enter in a new console --
```
export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
cd kafka_2.13-3.5.0
bin/kafka-server-start.sh config/server.properties
```
It is pointing to private server , change server.properties so that it can run in public IP 

To do this , you can follow any of the 2 approaches shared belwo --
Do a "sudo nano config/server.properties" - change ADVERTISED_LISTENERS to public ip of the EC2 instance


Create the topic:
-----------------------------
Duplicate the session & enter in a new console --
```
cd kafka_2.13-3.5.0
bin/kafka-topics.sh --create --topic demo_test --bootstrap-server <Public IP>:9092 --replication-factor 1 --partitions 1
```
Start Producer:
--------------------------
```
bin/kafka-console-producer.sh --topic demo_test --bootstrap-server <Public IP>:9092 
```
Start Consumer:
-------------------------
Duplicate the session & enter in a new console --
```
cd kafka_2.13-3.5.0
bin/kafka-console-consumer.sh --topic demo_test --bootstrap-server <Public IP>:9092
```

@echo off
echo =========================
echo Starting Zookeeper...
echo =========================
cd C:\kafka
start cmd /k ".\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties"
timeout /t 5 >nul

echo =========================
echo Starting Kafka Broker...
echo =========================
cd C:\kafka
start cmd /k ".\bin\windows\kafka-server-start.bat .\config\server.properties"
timeout /t 10 >nul

echo =========================
echo Starting Kafka Producer...
echo =========================
cd C:\kafka\bin\windows
start cmd /k "kafka-console-producer.bat --topic smartphoneTopic --bootstrap-server localhost:9092"
timeout /t 2 >nul

echo =========================
echo Starting Kafka Consumer...
echo =========================
cd C:\kafka\bin\windows
start cmd /k "kafka-console-consumer.bat --topic smartphoneTopic --from-beginning --bootstrap-server localhost:9092"
timeout /t 2 >nul

echo =========================
echo Starting Hadoop Services...
echo =========================
start cmd /k "start-all"
timeout /t 10 >nul

echo =========================
echo Starting HBase...
echo =========================
cd C:\hadoop-3.3.0\hbase\bin
start cmd /k "start-hbase"
timeout /t 5 >nul

echo =========================
echo Starting HBase Thrift Server...
echo =========================
start cmd /k "hbase thrift start"
timeout /t 2 >nul

echo =========================
echo Check services
echo =========================
start cmd /k "jps"
timeout /t 2 >nul

echo =========================
echo All services are started!
echo =========================
pause


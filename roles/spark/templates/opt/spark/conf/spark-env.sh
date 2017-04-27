SPARK_MASTER_OPTS="-Dspark.deploy.defaultCores=1"
SPARK_WORKER_OPTS="-Dspark.worker.cleanup.enabled=true -Dspark.worker.cleanup.interval=7200"
SPARK_DAEMON_JAVA_OPTS="-Dspark.deploy.recoveryMode=ZOOKEEPER -Dspark.deploy.zookeeper.url=uat-zk-01:2181,uat-zk-02:2181,uat-zk-03:2181 -Dspark.deploy.zookeeper.dir=/spark"
export ZEPPELIN_PORT=30001

export SPARK_HOME=/opt/spark
export SPARK_SUBMIT_OPTIONS="--driver-cores 1 --driver-memory 1G --total-executor-cores 2 --files ${SPARK_HOME}/conf/hive-site.xml"

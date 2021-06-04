FROM docker.io/bitnami/spark:3-debian-10
RUN curl https://repo1.maven.org/maven2/org/mongodb/spark/mongo-spark-connector_2.12/3.0.1/mongo-spark-connector_2.12-3.0.1.jar --output /opt/bitnami/spark/jars/mongo-spark-connector_2.12-3.0.1.jar
RUN curl https://repo1.maven.org/maven2/org/mongodb/bson/4.0.5/bson-4.0.5.jar --output /opt/bitnami/spark/jars/bson-4.0.5.jar
RUN curl https://repo1.maven.org/maven2/org/mongodb/mongodb-driver-sync/4.0.5/mongodb-driver-sync-4.0.5.jar --output /opt/bitnami/spark/jars/mongodb-driver-sync-4.0.5.jar
RUN curl https://repo1.maven.org/maven2/org/mongodb/mongodb-driver-core/4.0.5/mongodb-driver-core-4.0.5.jar --output /opt/bitnami/spark/jars/mongodb-driver-core-4.0.5.jar
RUN curl https://repo1.maven.org/maven2/org/scala-lang/scala-library/2.12.11/scala-library-2.12.11.jar --output /opt/bitnami/spark/jars/scala-library-2.12.11.jar 
RUN curl https://repo1.maven.org/maven2/org/apache/spark/spark-streaming_2.12/3.0.1/spark-streaming_2.12-3.0.1.jar --output /opt/bitnami/spark/jars/spark-streaming_2.12-3.0.1.jar 
RUN curl https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.0.1/spark-sql-kafka-0-10_2.12-3.0.1.jar --output /opt/bitnami/spark/jars/spark-sql-kafka-0-10_2.12-3.0.1.jar 
RUN curl https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.8.2.0/kafka-clients-0.8.2.0.jar --output /opt/bitnami/spark/jars/kafka-clients-0.8.2.0.jar
RUN curl https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.9.0/commons-pool2-2.9.0.jar --output /opt/bitnami/spark/jars/commons-pool2-2.9.0.jar 
COPY spark-token-provider-kafka-0-10_2.12-3.0.1.jar /opt/bitnami/spark/jars/spark-token-provider-kafka-0-10_2.12-3.0.1.jar
COPY kafka-clients-2.4.1.jar /opt/bitnami/spark/jars/kafka-clients-2.4.1.jar
COPY analysis/*.py /analysis/
COPY log4j.properties /opt/bitnami/spark/conf/log4j.properties

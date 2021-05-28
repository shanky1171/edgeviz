FROM docker.io/bitnami/spark:3-debian-10
RUN curl https://repo1.maven.org/maven2/org/mongodb/spark/mongo-spark-connector_2.12/3.0.1/mongo-spark-connector_2.12-3.0.1.jar --output /opt/bitnami/spark/jars/mongo-spark-connector_2.12-3.0.1.jar
RUN curl https://repo1.maven.org/maven2/org/mongodb/bson/4.0.5/bson-4.0.5.jar --output /opt/bitnami/spark/jars/bson-4.0.5.jar
RUN curl https://repo1.maven.org/maven2/org/mongodb/mongodb-driver-sync/4.0.5/mongodb-driver-sync-4.0.5.jar --output /opt/bitnami/spark/jars/mongodb-driver-sync-4.0.5.jar
RUN curl https://repo1.maven.org/maven2/org/mongodb/mongodb-driver-core/4.0.5/mongodb-driver-core-4.0.5.jar --output /opt/bitnami/spark/jars/mongodb-driver-core-4.0.5.jar
RUN curl https://repo1.maven.org/maven2/org/scala-lang/scala-library/2.12.11/scala-library-2.12.11.jar --output /opt/bitnami/spark/jars/scala-library-2.12.11.jar 
COPY analysis/df1.py /analysis/

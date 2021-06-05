from datetime import datetime as dt
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
from pyspark.sql.functions import *
from pyspark.sql.types import *


#### Create Session   
ss = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1") \
    .getOrCreate()


schema = StructType() \
        .add("current", IntegerType()) \
        .add("vibration_x", IntegerType()) \
        .add("vibration_y", IntegerType()) \
        .add("suction_pressure", IntegerType()) \
        .add("reactor_level", IntegerType()) \
        .add("recycle_flow", IntegerType()) \
        .add("seal_level", IntegerType()) \
        .add("hexane_seal_flow", IntegerType()) \
        .add("level_control", IntegerType()) \
        .add("asset_running_state", IntegerType()) \
        .add("ts", StringType()) 

#### Read Stream Setup Session   
df = ss \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka:9092") \
  .option("subscribe", "sample") \
  .load() 

#df1=df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
#df1=df.selectExpr("CAST(value AS STRING)")

df1 = df.select(from_json(col("value").cast("string"),schema).alias("sensor"))
df1.printSchema()

df3 = df1.select(col("sensor.*"))
df3.printSchema()

#### Transformed Incoming Data Source  
df3 = df3.withColumn("tstamp", to_timestamp(col("ts"), 'MM-dd-yyyy HH:mm:ss'))
df3.printSchema()

#### Transformed Incoming Data Sink  
df3 \
.writeStream \
.trigger(processingTime='10 seconds') \
.option("truncate",'false') \
.outputMode("append") \
.format("console") \
.start() 

#### Tumbling Window Aggregation - Begin 
#df11 = df3 \
#         .groupby( \
#           window(col("tstamp"), windowDuration="10 seconds") \
#         ) \
#         .min("current","vibration_x","vibration_y", \
#              "suction_pressure", "reactor_level", "recycle_flow", \
#              "seal_level","hexane_seal_flow", "level_control" \
#         ) 

#df11.printSchema()

df15 = df3 \
         .groupby( \
           window(col("tstamp"), windowDuration="10 seconds") \
         ) \
         .min("current","vibration_x","vibration_y", \
              "suction_pressure", "reactor_level", "recycle_flow", \
              "seal_level","hexane_seal_flow", "level_control" \
         ) 

df17 = df3 \
         .groupby( \
           window(col("tstamp"), windowDuration="10 seconds") \
         ) \
         .max("current","vibration_x","vibration_y", \
              "suction_pressure", "reactor_level", "recycle_flow", \
              "seal_level","hexane_seal_flow", "level_control" \
         ) 

df21 = df3 \
         .groupby( \
           window(col("tstamp"), windowDuration="10 seconds") \
         ) \
         .avg("current","vibration_x","vibration_y", \
              "suction_pressure", "reactor_level", "recycle_flow", \
              "seal_level","hexane_seal_flow", "level_control" \
         ) 

#### Tumbling Window Aggregation - End 


#### Tumbling Window Sinks - Begin 

#df11 \
#.writeStream \
#.trigger(processingTime='10 seconds') \
#.option("truncate",'false') \
#.outputMode("update") \
#.format("console") \
#.start() 

qry15 = df15 \
.selectExpr("to_json(struct(*)) AS value") \
.writeStream \
.trigger(processingTime='10 seconds') \
.option("truncate",'false') \
.outputMode("update") \
.format("kafka") \
.option("kafka.bootstrap.servers", "kafka:9092") \
.option("topic", "minData") \
.option("checkpointLocation", "checkpoint/kafka_checkpoint15") \
.start() 

qry17 = df17 \
.selectExpr("to_json(struct(*)) AS value") \
.writeStream \
.trigger(processingTime='10 seconds') \
.option("truncate",'false') \
.outputMode("update") \
.format("kafka") \
.option("kafka.bootstrap.servers", "kafka:9092") \
.option("topic", "maxData") \
.option("checkpointLocation", "checkpoint/kafka_checkpoint17") \
.start() 

qry21 = df21 \
.selectExpr("to_json(struct(*)) AS value") \
.writeStream \
.trigger(processingTime='10 seconds') \
.option("truncate",'false') \
.outputMode("update") \
.format("kafka") \
.option("kafka.bootstrap.servers", "kafka:9092") \
.option("topic", "avgData") \
.option("checkpointLocation", "checkpoint/kafka_checkpoint21") \
.start() 

#### Tumbling Window Sinks - End 

qry15.awaitTermination()
qry17.awaitTermination()
qry21.awaitTermination()
#ss.streams.awaitAnyTermination()

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
        .add("devname", StringType()) \
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

'''
df15 = df3 \
         .groupby( \
           window(col("tstamp"), windowDuration="10 seconds"), \
           col("devname")
         ) \
         .min("current","vibration_x","vibration_y", \
              "suction_pressure", "reactor_level", "recycle_flow", \
              "seal_level","hexane_seal_flow", "level_control" \
         ) 
'''

df15 = df3 \
         .groupby( \
           window(col("tstamp"), windowDuration="10 seconds"), \
           col("devname")
         ) \
         .agg( \
           min("current").alias("min_current"), \
           min("vibration_x").alias("min_vibration_x"), \
           min("vibration_y").alias("min_vibration_y"), \
           min("suction_pressure").alias("min_suction_pressure"), \
           min("reactor_level").alias("min_reactor_level"), \
           min("recycle_flow").alias("min_recycle_flow"), \
           min("seal_level").alias("min_seal_level"), \
           min("hexane_seal_flow").alias("min_hexane_seal_flow"), \
           min("level_control").alias("min_level_control") \
         )

df17 = df3 \
         .groupby( \
           window(col("tstamp"), windowDuration="10 seconds"), \
           col("devname")
         ) \
         .agg( \
           max("current").alias("max_current"), \
           max("vibration_x").alias("max_vibration_x"), \
           max("vibration_y").alias("max_vibration_y"), \
           max("suction_pressure").alias("max_suction_pressure"), \
           max("reactor_level").alias("max_reactor_level"), \
           max("recycle_flow").alias("max_recycle_flow"), \
           max("seal_level").alias("max_seal_level"), \
           max("hexane_seal_flow").alias("max_hexane_seal_flow"), \
           max("level_control").alias("max_level_control") \
         ) 

df21 = df3 \
         .groupby( \
           window(col("tstamp"), windowDuration="10 seconds"), \
           col("devname")
         ) \
         .agg( \
           avg("current").alias("avg_current"), \
           avg("vibration_x").alias("avg_vibration_x"), \
           avg("vibration_y").alias("avg_vibration_y"), \
           avg("suction_pressure").alias("avg_suction_pressure"), \
           avg("reactor_level").alias("avg_reactor_level"), \
           avg("recycle_flow").alias("avg_recycle_flow"), \
           avg("seal_level").alias("avg_seal_level"), \
           avg("hexane_seal_flow").alias("avg_hexane_seal_flow"), \
           avg("level_control").alias("avg_level_control") \
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

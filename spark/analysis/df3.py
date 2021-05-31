from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
from pyspark.sql.functions import *
from pyspark.sql.types import *


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

df = ss \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "127.0.0.1:9092") \
  .option("subscribe", "sample") \
  .load() 

#df1=df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
#df1=df.selectExpr("CAST(value AS STRING)")
df1 = df.select(from_json(col("value").cast("string"),schema).alias("sensor"))
df3 = df1.select(col("sensor.*"))
#df3 = df1.select(avg(col("sensor.current")))

df5 = df1.select( \
                 avg(col("sensor.current")).alias("avg_current"), \
                 avg(col("sensor.vibration_x")).alias("avg_vib_x"), \
                 avg(col("sensor.vibration_y")).alias("avg_vib_y"), \
                 avg(col("sensor.suction_pressure")).alias("avg_suct_pressure"), \
                 avg(col("sensor.reactor_level")).alias("avg_reactor_lvl"), \
                 avg(col("sensor.recycle_flow")).alias("avg_recycle_flow"), \
                 avg(col("sensor.seal_level")).alias("avg_seal_level"), \
                 avg(col("sensor.hexane_seal_flow")).alias("avg_hexane_seal_fl"), \
                 avg(col("sensor.level_control")).alias("avg_lvl_control") \
                 )

df7 = df1.select( \
                 max(col("sensor.current")).alias("max_current"), \
                 max(col("sensor.vibration_x")).alias("max_vib_x"), \
                 max(col("sensor.vibration_y")).alias("max_vib_y"), \
                 max(col("sensor.suction_pressure")).alias("max_suct_pressure"), \
                 max(col("sensor.reactor_level")).alias("max_reactor_lvl"), \
                 max(col("sensor.recycle_flow")).alias("max_recycle_flow"), \
                 max(col("sensor.seal_level")).alias("max_seal_level"), \
                 max(col("sensor.hexane_seal_flow")).alias("max_hexane_seal_fl"), \
                 max(col("sensor.level_control")).alias("max_lvl_control") \
                 )


df9 = df1.select( \
                 min(col("sensor.current")).alias("min_current"), \
                 min(col("sensor.vibration_x")).alias("min_vib_x"), \
                 min(col("sensor.vibration_y")).alias("min_vib_y"), \
                 min(col("sensor.suction_pressure")).alias("min_suct_pressure"), \
                 min(col("sensor.reactor_level")).alias("min_reactor_lvl"), \
                 min(col("sensor.recycle_flow")).alias("min_recycle_flow"), \
                 min(col("sensor.seal_level")).alias("min_seal_level"), \
                 min(col("sensor.hexane_seal_flow")).alias("min_hexane_seal_fl"), \
                 min(col("sensor.level_control")).alias("min_lvl_control") \
                 )

df3 \
.writeStream \
.trigger(processingTime='6 seconds') \
.option("truncate",'false') \
.outputMode("append") \
.format("console") \
.start() 

df5 \
.writeStream \
.trigger(processingTime='6 seconds') \
.option("truncate",'false') \
.outputMode("complete") \
.format("console") \
.start() 

df7 \
.writeStream \
.trigger(processingTime='6 seconds') \
.option("truncate",'false') \
.outputMode("complete") \
.format("console") \
.start() 

df9 \
.writeStream \
.trigger(processingTime='6 seconds') \
.option("truncate",'false') \
.outputMode("complete") \
.format("console") \
.start() 

ss.streams.awaitAnyTermination()

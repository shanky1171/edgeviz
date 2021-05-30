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
#  .select(from_json(col("value").cast("string"), schema).alias("parsed_value"))
#  .writeStream \
#  .format("console") \
#  .outputMode("update") \
#  .start() \
#  .awaitTermination()

#df1=df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
#df1=df.selectExpr("CAST(value AS STRING)")
df1 = df.select(from_json(col("value").cast("string"),schema).alias("sensor"))
#df3 = df1.select(col("sensor.*"))
df3 = df1.select(avg(col("sensor.current")))

df3 \
.writeStream \
.trigger(processingTime='6 seconds') \
.option("truncate",'false') \
.outputMode("update") \
.format("console") \
.start() \
.awaitTermination()


#ssc = StreamingContext(sc, 10)


#ssc.start()
#ssc.awaitTermination()

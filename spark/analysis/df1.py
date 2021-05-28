from pyspark.sql import SparkSession
from pyspark.sql.functions import date_trunc

spark = SparkSession \
    .builder \
    .appName("df1") \
    .config("spark.mongodb.input.uri", "mongodb://edgedbuser:edgedb@10.0.0.25:27017/edgedb.tspump") \
    .config("spark.mongodb.output.uri", "mongodb://edgedbuser:edgedb@10.0.0.25:27017/edgedb.tspumpO") \
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1") \
    .getOrCreate()

df = spark.read.format("com.mongodb.spark.sql.DefaultSource").load()

df.printSchema() 
df.show(10) 

#To remove the seconds data from the frame
df1=df.withColumn('hour', date_trunc("minute","ts"))

#To show the aggregation done on the grouped data 
df1.groupby('hour').mean().show()

#To select the avg values 
df2=df1.groupby('hour').mean()
df2.select('hour','avg(current)').show()

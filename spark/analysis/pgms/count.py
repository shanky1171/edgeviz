from pyspark import SparkContext
from operator import add
sc = SparkContext("local", "count app")
words = sc.parallelize (
   ["scala", 
   "java", 
   "hadoop", 
   "spark", 
   "akka",
   "spark vs hadoop", 
   "pyspark",
   "pyspark and spark"]
)
counts = words.count()
print("count(): Number of elements in RDD -> %i" % (counts))

coll = words.collect()
print("collect():Elements in RDD -> %s" % (coll))

print("foreach() Begin:")
def f(x): print(x)
fore = words.foreach(f) 
print("foreach() End:")

words_filter = words.filter(lambda x: 'spark' in x)
filtered = words_filter.collect()
print("filter():Fitered RDD -> %s" % (filtered))

words_map = words.map(lambda x: (x, 1))
mapping = words_map.collect()
print("map():Key value pair -> %s" % (mapping))

nums = sc.parallelize([1, 2, 3, 4, 5])
adding = nums.reduce(add)
print("reduce(): Adding all the elements -> %i" % (adding))

x = sc.parallelize([("spark", 1), ("hadoop", 4)])
y = sc.parallelize([("spark", 2), ("hadoop", 5)])
joined = x.join(y)
final = joined.collect()
print("join():Join RDD -> %s" % (final))

words.cache() 
caching = words.persist().is_cached 
print("cache():Words got chached > %s" % (caching))

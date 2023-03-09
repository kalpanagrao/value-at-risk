# this is a test file
pip install pyspark
import pyspark
import pandas as pd
df = pd.read_csv(r'C:\Users\User\Desktop\Kalpana\Python_Pyspark\kalp_files\test.csv')
print(df)
type(df)
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Practise').getOrCreate()
spark

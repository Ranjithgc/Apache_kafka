"""
@Author: Ranjith G C
@Last Modified by: Ranjith G C
@Last Modified time: 2021-08-07 
@Title : Program Aim is to work stock live data and saving output to text file
"""
from kafka import KafkaConsumer
import pydoop.hdfs as hdfs

consumer = KafkaConsumer('testTopic')
hdfs_path = 'hdfs://localhost:9000/kafka_stock_data/data.txt'
for message in consumer:
    values = message.value
    with hdfs.open(hdfs_path, 'at') as f:    
        f.write(f"{values}\n")

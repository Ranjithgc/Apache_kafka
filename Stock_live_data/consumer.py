"""
@Author: Ranjith G C
@Last Modified by: Ranjith G C
@Last Modified time: 2021-08-07 
@Title : Program Aim is to work stock live data and saving output to text file
"""
import sys
from kafka import KafkaConsumer
consumer = KafkaConsumer('testTopic')
sys.stdout = open("stock.txt", "w")
for message in consumer:
    values = message.value
    print(values)

sys.stdout.close()
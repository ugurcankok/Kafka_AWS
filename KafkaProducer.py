import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json

producer = KafkaProducer(bootstrap_servers=[':9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

producer.send('demo_test', value={'surnasdasdame':'parasdasdmar'})

df = pd.read_csv("data/indexProcessed.csv")

while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send('demo_test', value=dict_stock)
    producer.flush() #clear data from kafka server
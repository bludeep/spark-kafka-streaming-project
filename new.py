import pandas as pd
import json
import time
KAFKA_SERVER = 'kafka:9092'
TOPIC_NAME = 'csv-data'
CSV_FILE = 'D:\DEV\spark streaming project\portugal_listinigs.csv'
RECORD_PER_SECOND = 10


def send_csv_to_kafka():
    """ producer = KafkaProducer(
        bootstrap_server=KAFKA_SERVER,
        value_serializer=lambda x: json.dumps(x).encode("utf-8")
    ) """

    df = pd.read_csv(CSV_FILE)

    for index, row in df.iterrows():

        message = row.to_dict()
        key = f'{row["District"]}_{row['Type']}'
        print(key.encode("utf-8"))

        """ producer.send(TOPIC_NAME, message) """

        time.sleep(1 / RECORD_PER_SECOND)


send_csv_to_kafka()

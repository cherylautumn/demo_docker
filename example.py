#!/usr/bin/env python
import threading, logging, time

from kafka import KafkaConsumer, KafkaProducer


class Producer(threading.Thread):
    daemon = True

    def run(self):
        print("connect to 54.172.25.150")
        producer = KafkaProducer(bootstrap_servers='54.172.25.150:9092', request_timeout_ms=120000)

        while True:
            print("send data to broker")
            producer.send('my-topic', b"test")
            producer.send('my-topic', b"\xc2Hola, mundo!")
            time.sleep(1)


class Consumer(threading.Thread):
    daemon = True

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers='54.172.25.150:9092',
                                 auto_offset_reset='earliest',
                                 request_timeout_ms=120000)
        consumer.subscribe(['my-topic'])

        for message in consumer:
            print("*****")
            print (message)


def main():
    threads = [
        Producer(),
        Consumer()
    ]

    for t in threads:
        t.start()

    time.sleep(10)

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    main()

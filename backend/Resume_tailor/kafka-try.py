from confluent_kafka import Producer, Consumer, KafkaException, KafkaError
import time

# Kafka Configuration
KAFKA_BROKER = "34.47.252.137:9092"  # Update this if Kafka is in a different container
TOPIC = "test-topic"

# Create Kafka Producer
producer_conf = {'bootstrap.servers': KAFKA_BROKER}
producer = Producer(producer_conf)

def delivery_report(err, msg):
    """Callback for message delivery reports"""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Produce Messages
for i in range(5):
    message = f"Hello Kafka {i}"
    producer.produce(TOPIC, key=str(i), value=message, callback=delivery_report)
    time.sleep(1)

producer.flush()  # Ensure all messages are sent
print("Produced messages successfully.")

# Create Kafka Consumer
consumer_conf = {
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': 'my-consumer-group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_conf)
consumer.subscribe([TOPIC])

print("Consuming messages...")
try:
    while True:
        msg = consumer.poll(1.0)  # Wait for message
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                raise KafkaException(msg.error())
        
        print(f"Received message: {msg.value().decode('utf-8')}")

except KeyboardInterrupt:
    print("Stopping consumer...")
finally:
    consumer.close()

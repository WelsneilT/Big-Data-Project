from kafka import KafkaProducer

bootstrap_servers = 'localhost:9092'
topic = 'smartphoneTopic'

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

def send_message(message):
    try:
        producer.send(topic,str(message).encode('ISO-8859-1'))
        print(f"Produced: {message} to Kafka topic: {topic}")
    except Exception as error:
        print(f"Error: {error}")
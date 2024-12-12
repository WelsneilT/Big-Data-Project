from kafka import KafkaProducer
import json

# Khởi tạo Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Địa chỉ Kafka broker
    value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode('utf-8')  # Serialize dữ liệu thành JSON
)

# Dữ liệu thử dạng danh sách
data_list = [
    ['62', 'Oppo', 'A78 ', '6.43', '8', '256', '50MP', 'Dual', '0', '3%', '0', 'Gaff Electronics Kenya', '94%', '165', 'No reviews'],
    ['146', 'Samsung', 'Galaxy A04e ', '6.5', '3', '32', '13MP + 2MP + 5MP', 'Dual', '0', '29%', '0', 'Minestar', '86%', '1002', 'No reviews']
]

# Gửi từng bản ghi vào Kafka topic 'smartphoneTopic'
for data in data_list:
    producer.send('smartphoneTopic', value=data)

# Đảm bảo dữ liệu đã được gửi
producer.flush()
print("Dữ liệu đã được gửi vào Kafka topic.")

import sys
import time

sys.path.append('C:/Downloads/Big-Data-Project/Main')
sys.path.append(r'C:/Downloads/Big-Data-Project/Main/Lambda/Stream_data')

from Lambda.producer import send_message
from ML_consumer import consum
import threading
from Lambda.Stream_data.stream_data import generate_real_time_data

def generate_real_time_data(file):
    try:
        # Giả sử file là file mở, bạn có thể đọc dòng hoặc dữ liệu từ đây
        # Chẳng hạn lấy dòng đầu tiên và chuyển thành dict
        line = file.readline().strip()  # Đọc dòng đầu tiên
        columns = line.split(',')  # Giả sử là CSV với dấu phẩy
        data = {
            "id": columns[0],
            "brand": columns[1],
            "model_name": columns[2],
            "screen_size": float(columns[3]),
            "ram": int(columns[4]),
            "rom": int(columns[5]),
            "cams": columns[6],
            "sim_type": columns[7],
            "battery_capacity": int(columns[8]),
            "sale_percentage": int(columns[9].replace('%', '')),
            "product_rating": float(columns[10]),
            "seller_name": columns[11],
            "seller_score": columns[12],
            "seller_followers": int(columns[13]),
            "reviews": columns[14]
        }

        # Trả về một chuỗi JSON
        return json.dumps(data)

    except Exception as e:
        print(f"Error in generate_real_time_data: {str(e)}")
        return None
    
def producer_thread():
    while True:
        try:
            file_path = 'C:/Downloads/Big-Data-Project/Main/Lambda/Stream_data/stream_data.csv'
            with open(file_path, 'r', encoding='ISO-8859-1', errors='ignore') as file:
                lines = file.readlines()
                print(lines[:2])  # In ra 5 dòng đầu tiên
                message = generate_real_time_data(file)

                


            send_message(message)
            print("Message sent to Kafka topic")

            # Sleep for 5 seconds before collecting and sending the next set of data
            time.sleep(5)

        except Exception as e:
            print(f"Error in producer_thread: {str(e)}")

def consumer_thread():
    while True:
        try:
            consum()
            # Sleep for a short interval before consuming the next message
            time.sleep(3)
        except Exception as e:
            print(f"Error in consumer_thread: {str(e)}")

# Create separate threads for producer and consumer
producer_thread = threading.Thread(target=producer_thread)
consumer_thread = threading.Thread(target=consumer_thread)

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for the threads to finish (which will never happen in this case as they run infinitely)
producer_thread.join()
consumer_thread.join()
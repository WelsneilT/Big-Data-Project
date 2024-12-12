import sys
import time

sys.path.append('C:/Downloads/Big-Data-Project/Main')
sys.path.append(r'C:/Downloads/Big-Data-Project/Main/Lambda/Stream_data')

from Lambda.producer import send_message
from ML_consumer import consum
import threading
from Lambda.Stream_data.stream_data import generate_real_time_data

def producer_thread():
    while True:
        try:
            file_path = 'C:/Downloads/Big-Data-Project/Main/Lambda/Stream_data/stream_data.csv'
            with open(file_path, 'r', encoding='ISO-8859-1', errors='ignore') as file:
                lines = file.readlines()
                print(lines[:5])  # In ra 5 dòng đầu tiên
                message = generate_real_time_data(file)

                if message:  # Nếu message không phải là None
                    send_message(message)
                    print(f"Produced: {message} to Kafka topic: smartphoneTopic")
                else:
                    print("No valid data to produce.")

                break

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
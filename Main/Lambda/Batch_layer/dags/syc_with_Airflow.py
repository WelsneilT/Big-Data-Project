import sys
import os
import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# Thêm thư mục chứa Batch_layer vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Batch_layer')))

# Import hàm batch_layer từ module batch_layer
from batch_layer import batch_layer

# Định nghĩa DAG
with DAG(
    dag_id="daily_data_sync",
    start_date=datetime.datetime(2024, 3, 29),
    schedule_interval="*/1 * * * *",  # Run every 1 minute
) as dag:

    # Sử dụng PythonOperator để gọi hàm batch_layer
    batch_layer_task = PythonOperator(
        task_id="batch_layer",
        python_callable=batch_layer  # Chỉ cần tham chiếu đến hàm batch_layer
    )


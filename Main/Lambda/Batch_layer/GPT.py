import csv
import psycopg2

# Kết nối tới PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="Big-Data-Project",
    user="postgres",
    password="belieber"
)
cur = conn.cursor()

# Đọc dữ liệu từ file CSV
csv_file_path = r"C:\Downloads\Big-Data-Project\Main\Lambda\Stream_data\stream_data.csv"  # Đường dẫn đến file CSV
with open(csv_file_path, 'r', encoding='ISO-8859-1') as file:  # Sử dụng encoding khác
    reader = csv.DictReader(file)  # Đọc dữ liệu theo dạng dictionary

    for row in reader:
        try:
            # Chuyển đổi kiểu dữ liệu từ chuỗi sang số nếu cần
            model_id = int(row["id"])
            brand = row["brand"]
            model_name = row["model_name"]
            screen_size = float(row["screen_size"])
            ram_size = int(row["ram"])
            storage_size = int(row["rom"])
            camera_specs = row["cams"]
            camera_type = row["sim_type"]
            battery_capacity = int(row["battary"])  # Chú ý 'battary' là tên cột

            # Loại bỏ ký tự '%' trong sale_percentage và seller_score
            discount_percentage = float(row["sale_percentage"].replace('%', '').replace(',', ''))  # Loại bỏ ký tự '%' và dấu phẩy nếu có
            product_rating = float(row["product_rating"])
            seller_name = row["seller_name"]
            seller_rating = float(row["seller_score"].replace('%', '').replace(',', ''))  # Loại bỏ ký tự '%'
            seller_followers = int(row["seller_followers"])
            reviews = row["Reviews"]

            # Kiểm tra nếu ID đã tồn tại
            cur.execute("SELECT 1 FROM phone WHERE id = %s", (model_id,))
            if cur.fetchone():
                print(f"ID {model_id} đã tồn tại, bỏ qua.")
                continue  # Bỏ qua nếu ID đã tồn tại trong cơ sở dữ liệu

            # Chèn dữ liệu vào PostgreSQL
            cur.execute("""
                INSERT INTO phone (id, brand, model_name, screen_size, ram, rom, cams, sim_type, battery, sale_percentage, product_rating, seller_name, seller_score, seller_followers, reviews)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (model_id, brand, model_name, screen_size, ram_size, storage_size, camera_specs, camera_type, battery_capacity, discount_percentage, product_rating, seller_name, seller_rating, seller_followers, reviews))

            # Commit vào cơ sở dữ liệu
            conn.commit()
            print(f"Đã chèn dữ liệu vào bảng: {model_id}")

        except Exception as e:
            print(f"Lỗi khi chèn dữ liệu: {e}")
            conn.rollback()  # Rollback nếu có lỗi

# Đóng kết nối
cur.close()
conn.close()

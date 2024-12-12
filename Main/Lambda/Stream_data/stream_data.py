import csv
import random




def generate_real_time_data(file_path):
    with open(file_path, 'r',  encoding='ISO-8859-1', errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)


        random_index = random.randint(1, len(data) - 1)
        random_data = data[random_index]

        return random_data









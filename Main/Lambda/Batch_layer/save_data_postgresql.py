import pandas as pd
from sqlalchemy import create_engine

def save_data(data):

    engine = create_engine('postgresql://postgres:belieber@localhost:5432/Big-Data-Project')

    data.to_sql('Phone', engine, if_exists='replace', index=False)

    print("data stored in postgresql")
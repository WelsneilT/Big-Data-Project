import pickle
import ast
import numpy as np

import xgboost as xgb

# Mappings
brand_mapping = {
    'Maxfone': 1, 'Infinix': 2, 'Freeyond': 3, 'XIAOMI': 4, 'Tecno': 5,
    'Oppo': 6, 'Nokia': 7, 'Samsung': 8, 'Huawei': 9, 'Vivo': 10,
    'Realme': 11, 'Sowhat': 12, 'Apple': 13
}
sim_type_mapping = {'Dual': 1, 'Single': 2}

numeric_to_brand = {v: k for k, v in brand_mapping.items()}
numeric_to_sim_type = {v: k for k, v in sim_type_mapping.items()}

def map_brand_to_numeric(brand):
    return brand_mapping.get(brand, 14)

def map_sim_type_to_numeric(sim_type):
    return sim_type_mapping.get(sim_type, 3)

def map_numeric_to_brand(number):
    return numeric_to_brand.get(number, 'Unknown')

def map_numeric_to_sim_type(number):
    return numeric_to_sim_type.get(number, 'Unknown')

def transformation(original_list):
    # Load model with error handling
    try:
        model = xgb.Booster()
     
        model = pickle.load(open('C:/Downloads/Big-Data-Project/Main/Lambda/ML_operations/xgb_model.pkl', 'rb'))
    except FileNotFoundError:
        raise FileNotFoundError("Model file not found at the specified path.")
    except pickle.UnpicklingError:
        raise ValueError("Error loading the model. Ensure it's a valid pickle file.")

    # Parse input
    

    # Transform input
    new_list = [
        map_brand_to_numeric(original_list[1]),
        float(original_list[3]),
        float(original_list[4]),
        float(original_list[5]),
        map_sim_type_to_numeric(original_list[7]),
        float(original_list[8])
    ]

    # Make prediction
    price = model.predict(np.array(new_list).reshape(1, -1))

    # Map back to original representation
    new_list[0] = map_numeric_to_brand(new_list[0])
    new_list[4] = map_numeric_to_sim_type(new_list[4])

    # Append predicted price
    new_list.extend(price)

    return new_list
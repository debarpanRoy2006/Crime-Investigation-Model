import os
import pickle
import pandas as pd

# Define the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "ml_model/dataset")

# ✅ Ensure the dataset directory exists
os.makedirs(DATASET_DIR, exist_ok=True)

# ✅ Load CSV files
cybercrime_df = pd.read_csv(os.path.join(BASE_DIR, 'datasets/cybercrime_laws_india.csv'))
murder_df = pd.read_csv(os.path.join(BASE_DIR, 'datasets/murder_laws_india.csv'))
rape_df = pd.read_csv(os.path.join(BASE_DIR, 'datasets/rape_laws_india.csv'))
property_df = pd.read_csv(os.path.join(BASE_DIR, 'datasets/property_crimes_with_steps.csv'))
robbery_df = pd.read_csv(os.path.join(BASE_DIR, 'datasets/robbery_laws_india.csv'))
public_order_df = pd.read_csv(os.path.join(BASE_DIR, 'datasets/public_order_crimes_india.csv'))
organized_df = pd.read_csv(os.path.join(BASE_DIR, 'datasets/organized_crimes_india.csv'))
kidnapping_df = pd.read_csv(os.path.join(BASE_DIR, 'datasets/kidnapping_crimes_india.csv'))
white_collar_df = pd.read_csv(os.path.join(BASE_DIR, 'datasets/white_collar_crimes_india.csv'))

# ✅ Rename columns for consistency
cybercrime_df.rename(columns={"IPC / IT Act": "IPC"}, inplace=True)
property_df.rename(columns={"Description": "Description of the Case"}, inplace=True)

# ✅ Add categories
datasets = [
    (cybercrime_df, 'Cybercrime'),
    (murder_df, 'Murder'),
    (rape_df, 'Rape'),
    (property_df, 'Property'),
    (robbery_df, 'Robbery'),
    (public_order_df, 'Public Order'),
    (organized_df, 'Organized Crime'),
    (kidnapping_df, 'Kidnapping'),
    (white_collar_df, 'White Collar')
]

for df, category in datasets:
    df['Category'] = category

# ✅ Combine all datasets into one DataFrame
combined_df = pd.concat([df for df, _ in datasets], ignore_index=True)

# ✅ Save the combined DataFrame using pickle
pickle.dump(combined_df, open(os.path.join(DATASET_DIR, "combined_data.sav"), "wb"))

print("✔ Data successfully saved!")

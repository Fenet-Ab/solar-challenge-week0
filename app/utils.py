import pandas as pd
import os

# Load cleaned data
def load_data():
    # Get the directory where this file is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Get the parent directory (project root)
    project_root = os.path.dirname(current_dir)
    # Construct data directory path
    data_dir = os.path.join(project_root, "data")
    
    benin = pd.read_csv(os.path.join(data_dir, "benin_clean.csv"))
    togo = pd.read_csv(os.path.join(data_dir, "togo_clean.csv"))
    sierra = pd.read_csv(os.path.join(data_dir, "sierra_clean.csv"))

    benin['Country'] = 'Benin'
    togo['Country'] = 'Togo'
    sierra['Country'] = 'Sierra Leone'

    df_all = pd.concat([benin, togo, sierra])
    return df_all

# Summary stats table
def summary_table(df, metric):
    return df.groupby('Country')[metric].agg(['mean','median','std']).round(2)

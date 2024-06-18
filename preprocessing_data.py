# ===================================================================================================================================================
# ========================================================== IMPORTING LIBRARY SECTION ==============================================================
# ===================================================================================================================================================


# ===================== IMPORTNG LIBRARIES =====================
import pandas as pd
import numpy as np



# ===================== CAR PURCHASE DATASET ====================
# loading given dataset --> using csv as xlsx file not loading
df_cpd = pd.read_csv("Car_Purchasing_Data.csv")


def cpd_preprocessing_input_data(df_cpd):
    irrelevant_columns = ['Customer Name','Customer e-mail','Country', 'Car Purchase Amount']
    input_used_columns = ['Gender', 'Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth']
    
    dropped_columns = [
        col for col in df_cpd.columns if col in irrelevant_columns
        ]
    
    remainder_columns = [
        col for col in df_cpd.columns if col not in dropped_columns
        ]
    
    return df_cpd[remainder_columns], dropped_columns, remainder_columns



def cpd_preprocessing_output_data(df_cpd):
    irrelevant_columns = ['Customer Name', 'Customer e-mail', 'Country', 'Gender', 'Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth']
    output_used_columns = ['Car Purchase Amount']
    
    dropped_columns = [
        col for col in df_cpd.columns if col in irrelevant_columns
        ]
    
    remainder_columns = [
        col for col in df_cpd.columns if col not in dropped_columns
        ]
    
    return df_cpd[remainder_columns], dropped_columns, remainder_columns
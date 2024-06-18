# ===================================================================================================================================================
# ========================================================== IMPORTING LIBRARY SECTION ==============================================================
# ===================================================================================================================================================


# ===================== IMPORTNG LIBRARIES =====================
import pytest
import pandas as pd
from preprocessing_data import cpd_preprocessing_input_data
from preprocessing_data import cpd_preprocessing_output_data



# ===================================================================================================================================================
# ============================================================== TEST CASES 1 =======================================================================
# ===================================================================================================================================================

# ===================== INPUT DATA =====================
# Input data - Verifying the input data doesn't contain unnecessary columns

def test_cpd_reprocess_input_columns():
    # ======================================== SHOWCASING  DATASET COLUMNS ========================================
    # all the coloumns in given dataset 
    all_columns = ['Customer Name', 'Customer e-mail', 'Country', 'Gender', 'Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount']
    df_cpd = pd.DataFrame(columns = all_columns)
    
    # declaring the original dataset shape and the shape after it has been processed
    original_dataset_shape = df_cpd.shape
    processed_cpd_df, dropped_columns, used_columns = cpd_preprocessing_input_data(df_cpd)
    
    # declaration of the intended output column out of all columns - irrelevant
    input_columns = ['Gender', 'Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth']
    
    # Assert that used columns match the expected utilised columns
    assert used_columns == input_columns, f"Expected used columns {input_columns}, but got {used_columns}."
    
    # Assert that no dropped column is in the used columns
    for col in dropped_columns:
        assert col not in used_columns, f"Column {col} should have been dropped but is still present in used columns."


    # ======================================== SHOWCASING DATASET SHAPE ========================================
    # Assert that the shape of the data is correct
    input_expected_dataset_shape = (original_dataset_shape[0], len(used_columns))
    print("\n\n")
    print(f"+++ PROCESSING INPUT DATASET SHAPE +++")
    print(f"The original dataset shape is --> {original_dataset_shape}")
    print(f"The dataset after being process is --> {processed_cpd_df.shape}")
    print(f"The dataset expected is --> {input_expected_dataset_shape}")


# ======================================== OUTPUT IN TERMINAL IF ERRORS ========================================    
    assert processed_cpd_df.shape == input_expected_dataset_shape, f"Expected shape is meant to be {input_expected_dataset_shape}, but instead got {processed_cpd_df.shape}."
   

if __name__ == "__main__":
    pytest.main()





# ===================================================================================================================================================
# ============================================================== TEST CASES 2 =======================================================================
# ===================================================================================================================================================


# ===================== OUTPUT DATA =====================
# Output data - Verifying the output data doesn't contain unnecessary columns

def test_cpd_reprocess_output_columns():
    # ======================================== SHOWCASING  DATASET COLUMNS ========================================
    # dataset columns before processing | dropped 
    all_columns = ['Customer Name', 'Customer e-mail', 'Country', 'Gender', 'Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount']
    df_cpd = pd.DataFrame(columns = all_columns)
    
    # stating the original dataset column and after it has been processed
    original_dataset_shape = df_cpd.shape
    processed_cpd_df, dropped_columns, used_columns = cpd_preprocessing_output_data(df_cpd)
    
    # intended output column
    output_columns = ['Car Purchase Amount']
    
    # Assert that used columns match the expected utilised columns
    assert used_columns == output_columns, f"Expected used columns {output_columns}, but got {used_columns}."
    
    # Assert that no dropped column is in the used columns
    for col in dropped_columns:
        assert col not in used_columns, f"Column {col} should have been dropped but is still present in used columns."

# ======================================== SHOWCASING DATASET SHAPE ========================================
    # Assert that the shape of the data is correct
    output_expected_dataset_shape = (original_dataset_shape[0], len(used_columns))
    print("\n\n")
    print(f"+++ PROCESSING OUTPUT DATASET SHAPE +++")
    print(f"The original dataset shape is --> {original_dataset_shape}")
    print(f"The dataset after being process is --> {processed_cpd_df.shape}")
    print(f"The dataset expected is --> {output_expected_dataset_shape}")


# ======================================== OUTPUT IN TERMINAL IF ERRORS ========================================    
    assert processed_cpd_df.shape == output_expected_dataset_shape, f"Expected shape is meant to be {output_expected_dataset_shape}, but instead got {processed_cpd_df.shape}."
   
if __name__ == "__main__":
    pytest.main()


# terminal syntax for running code
# pytest -s
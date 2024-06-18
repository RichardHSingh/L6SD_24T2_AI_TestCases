# Car Purchasing Data Preprocessing and Testing
This repository contains the implementation and testing of data preprocessing functions for a car purchasing dataset. The goal is to ensure that the dataset is correctly processed by removing irrelevant columns and verifying the structure of the resulting dataset.
<br><br><br>

# Testing
The testing script uses pytest to validate the preprocessing functions. It ensures that:
<br>
• The correct columns are retained in the processed data.
• The shape of the processed data matches the expected shape after irrelevant columns are dropped.
<br><br>

# Clone the repository.
• Place the Car_Purchasing_Data.csv file in the same directory.<br>
• Run the preprocessing functions as needed.<br>
• Use pytest to run the tests and verify the preprocessing --> _syntax - **pytest -s**_<br>
<br><br>

# Dependencies
• Virtual Environment
Syntax: python -m venv "name" --> python -m venv venv (it is industry practise to call the virtual environment venv)
Please make sure to activate the virtual enviroment --> venv\Scripts\activate

• Pandas
Syntax: pip install pandas

• Pytest
Syntax: pip install -U pytest

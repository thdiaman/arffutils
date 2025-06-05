import os
import pandas as pd
from filecmp import cmp
from arffutils import pandas_dataframe_to_arff, arff_to_pandas_dataframe, csv_to_arff, arff_to_csv

def test_pandas_dataframe_to_arff():
    # Load the CSV file into a DataFrame
    df = pd.read_csv("./tests/data.csv", dtype = {'Date': 'str', 'Product': 'str', 'ProductID': 'int', 'Category': 'category',
                                                  'Price': 'float', 'DiscountPercentage': 'int', 'IsOnSale': 'int'}) #, parse_dates = ["Date"])

    # Convert the DataFrame to ARFF file
    pandas_dataframe_to_arff(df, "./tests/temp.arff", relation_name="sales", label_name="IsOnSale")

    # Test the output    
    assert cmp("./tests/data.arff","./tests/temp.arff", shallow = False), "Test test_pandas_dataframe_to_arff failed"

def test_arff_to_pandas_dataframe():
    # Load the ARFF file into a DataFrame
    df = arff_to_pandas_dataframe("./tests/data.arff", dtype = {'Date': 'str', 'Product': 'str', 'ProductID': 'int',
                                    'Category': 'category', 'Price': 'float', 'DiscountPercentage': 'int', 'IsOnSale': 'int'})

    # Convert the DataFrame to CSV file
    df.to_csv("./tests/temp.csv", index=False)

    # Test the output    
    assert cmp("./tests/data.csv","./tests/temp.csv", shallow = False), "Test test_arff_to_pandas_dataframe failed"

def test_csv_to_arff():
    # Make the conversion
    csv_to_arff("./tests/data.csv", "./tests/temp.arff", dtype = {'Date': 'str', 'Product': 'str', 'ProductID': 'int',
                                    'Category': 'category', 'Price': 'float', 'DiscountPercentage': 'int', 'IsOnSale': 'int'}, 
                                    relation_name="sales", label_name="IsOnSale")

    # Test the output
    assert cmp("./tests/data.arff","./tests/temp.arff", shallow = False), "Test test_csv_to_arff failed"

def test_arff_to_csv():
    # Make the conversion
    arff_to_csv("./tests/data.arff","./tests/temp.csv")

    # Test the output
    assert cmp("./tests/data.csv","./tests/temp.csv", shallow = False), "Test test_arff_to_csv failed"

# Run the tests
test_pandas_dataframe_to_arff()
test_arff_to_pandas_dataframe()
test_arff_to_csv()
test_arff_to_csv()

# Clean up
os.remove("./tests/temp.arff") 
os.remove("./tests/temp.csv") 

import pandas as pd
from io import StringIO
import streamlit as st

class Dataset:
    def __init__(self,data=None):
        # Initialize Dataset attributes
        self.data = data  # Placeholder for dataset

    def set_data(self, file_path):
        # Logic to set data from file_path using pandas
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

                # Remove double quotes from each line
                lines = [line.replace('"', '') for line in lines]

                # Join the lines back into a single string
                cleaned_data = ''.join(lines)

                # Load the cleaned data into pandas DataFrame
                self.data = pd.read_csv(StringIO(cleaned_data), delimiter=';')
        except FileNotFoundError:
            print(f"File not found at path: {file_path}")
            self.data = None
        except Exception as e:
            print(f"An error occurred while loading the data: {e}")
            self.data = None

    def __getitem__(self, key):
        return self.data[key]
        
    def head_df(self):
        if self.data is not None:
            return self.data.head()
        else:
            return "No data available"
            
    def get_column(self, column_name):
        if self.data is not None:
            return self.data[column_name]
        else:
            return None
    def get_column_names(self):
        # Implement this method to return the column names of the dataset
        # For example:
        return list(self.data.columns)

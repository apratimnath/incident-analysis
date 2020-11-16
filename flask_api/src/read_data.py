'''
Created on Nov 16, 2020

@author: apratim
'''
import pandas as pd

data = None


def load_incident_data():
    # Importing the csv file
    global data
    print("Loading the data, and sending for cleaning.")
    data = pd.read_csv('../../datasets/incident_data.csv')
    data = clean_data()
    return data


def clean_data():
    global data
    print("Cleaning the data.")
    data.replace(['?'], 'Unknown', inplace=True)
    return data

    
if __name__ == '__main__':
    initial_data = load_incident_data()
    print("***********************Exploratoty Analysis*************************")
    print(initial_data.info())
    print("********************************************************************")

import pandas as pd
import numpy as np


# Function for loading, processing, and wrangling, and returning the processed form of the first dataset. It loads data, drops specified columns, drops rows with missing values, then applies the Primarystreamingservice function to make a new column, converts numbers in that column to float type, creates a new column that gives hours/day in %, and a new column that gives the overall mental health out of 100, and lastly, it orders all columns in the order specified:

def load_and_process(url_or_path_to_csv_file):

    
    def Primarystreamingservice(x):
        '''
        This function analyzes the given primary streaming service type, and assigns it a numerical value accordingly (numbers are easier to work with).
        '''
        if x['Primary streaming service']=="Spotify":
            return "1"
        elif x['Primary streaming service']=="Pandora": 
            return "2"  
        elif x['Primary streaming service']=="YouTube Music":
            return "3"
        elif x['Primary streaming service']=="Apple Music": 
            return "4"  
        elif x['Primary streaming service']=="I do not use a streaming service.":
            return "5"
        else: 
            return "6"  

        
        # Method Chain 1 (Load data and deal with missing data)

    datasetchain1 = (
                pd.read_csv('../data/raw/music_therapy_and_mental_health_survey_results (1).csv') \
                .drop(columns=['Timestamp', 'While working', 'Instrumentalist', 'Composer', 'Fav genre', 'Exploratory', 'Foreign languages', 'BPM', 'Frequency [Classical]', 'Frequency [Country]', 'Frequency [EDM]', 'Frequency [Folk]', 'Frequency [Gospel]', 'Frequency [Hip hop]', 'Frequency [Jazz]', 'Frequency [K pop]', 'Frequency [Latin]', 'Frequency [Lofi]', 'Frequency [Metal]', 'Frequency [Pop]', 'Frequency [R&B]', 'Frequency [Rap]', 'Frequency [Rock]', 'Frequency [Video game music]', 'Music effects', 'Permissions']) \
                .dropna() 
    )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    datasetchain2 = (
          datasetchain1
            .assign(Primary_streaming_service_in_numbers=lambda x: x.apply(Primarystreamingservice, axis="columns")) \
            .assign(Primary_streaming_service_in_numbers_float=lambda x: x['Primary_streaming_service_in_numbers'].astype(float)) \
            .assign(Hours_per_day_percentage=lambda x: x['Hours per day']/24 * 100) \
            .assign(Overall_Mental_Health_out_of_100=lambda x: (x['Anxiety'] + x['Depression'] + x['Insomnia'] + x['OCD'])*2.5) \
            .loc[:, ['Age', 'Primary streaming service', 'Primary_streaming_service_in_numbers', 'Hours_per_day_percentage', 'Anxiety', 'Depression', 'Insomnia', 'OCD', 'Overall_Mental_Health_out_of_100']]
    )

    
    # Make sure to return the latest dataframe

    return datasetchain2 




# Function for loading the second dataset (Student Mental Health), using method chaining:

def load_datasetsmh(url_or_path_to_csv_file):

    dataset_smh = pd.read_csv('../data/raw/Student_mental_health.csv') \
                .drop(columns=['Timestamp', 'Choose your gender', 'What is your course?', 'Marital status', 'Do you have Panic attack?', 'Did you seek any specialist for a treatment?']) \
                .dropna() \
                .assign(**{'Your current year of Study': lambda x: x['Your current year of Study'].str.lower(),
                          'What is your CGPA?': lambda x: x['What is your CGPA?'].str.strip()})
    return dataset_smh  

        # used the lower function since dataset was initially differentiating between lower and upper case (which was unideal, since, for example, year 4 means the same thing as Year 4)
        # used the strip function to ignore whitespace (because the '3.50 - 4.00' value appeared twice (since a survey-taker entered a space after))





# Function for the depression column, to be used when the categorical values are not ideal and numerical values are desired instead:

def depression(x):
    '''
    This function analyzes the "Do you have Depression?" column, and assigns the categorical values numerical values accordingly (numbers are easier to work with). Yes = 1 and No = 0.
    '''
    if x['Do you have Depression?']=="Yes":
        return "1"
    else: 
        return "0"  




# Function for the anxiety column, to be used when the categorical values are not ideal and numerical values are desired instead:

def anxiety(x):
    '''
    This function analyzes the "Do you have Anxiety?" column, and assigns the categorical values numerical values accordingly (numbers are easier to work with). Yes = 1 and No = 0.
    '''
    if x['Do you have Anxiety?']=="Yes":
        return "1"
    else: 
        return "0"  
    
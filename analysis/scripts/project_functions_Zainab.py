import pandas as pd

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
                .dropna(subset=['Age', 'Primary streaming service']) 
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


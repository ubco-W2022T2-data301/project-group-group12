import pandas as pd

def load_and_process(url_or_path_to_csv_file):

    
    def GenreConversion(x, genre):
        '''
        This function converts the string values of the specified genre column into numerical values to make them easier to analyze through data visualizations.
        '''
        if x[f'Frequency [{genre}]'] == "Never":
            return 1.0
        elif x[f'Frequency [{genre}]'] == "Rarely":
            return 4.0
        elif x[f'Frequency [{genre}]'] == "Sometimes":
            return 7.0
        else:
            return 10.0

        # Method Chain 1 (Load data and deal with missing data)

    methodchain1 = (
         pd.read_csv('../data/raw/music_therapy_and_mental_health_survey_results (1).csv')
        .drop(['Timestamp', 'Primary streaming service', 'Hours per day', 'While working', 'Instrumentalist', 'Composer', 'Exploratory', 'Foreign languages', 'BPM', 'Music effects', 'Permissions', 'Frequency [Gospel]', 'Frequency [Hip hop]', 'Frequency [K pop]', 'Frequency [Latin]', 'Frequency [Lofi]', 'Frequency [R&B]', 'Frequency [Video game music]', 'OCD'], axis="columns")
)


    # Method Chain 2 (Create new columns, drop others, and do processing)

    methodchain2 = (
          methodchain1
        .loc[(pd.read_csv('../data/raw/music_therapy_and_mental_health_survey_results (1).csv')['Age'] >= 15) & (pd.read_csv('../data/raw/music_therapy_and_mental_health_survey_results (1).csv')['Age'] <= 30)]
        .assign(**{f'Frequency_[{genre}]_num': pd.read_csv('../data/raw/music_therapy_and_mental_health_survey_results (1).csv').apply(lambda x: GenreConversion(x, genre), axis='columns') for genre in ['Classical', 'Country', 'EDM', 'Folk', 'Jazz', 'Metal', 'Pop', 'Rap', 'Rock']})
        .loc[~pd.read_csv('../data/raw/music_therapy_and_mental_health_survey_results (1).csv')['Fav genre'].str.contains('Gospel|Hip hop|K pop|Latin|Lofi|R&B|Video game music')]
        .drop(['Frequency [Classical]','Frequency [Country]', 'Frequency [EDM]', 'Frequency [Folk]', 'Frequency [Jazz]', 'Frequency [Metal]', 'Frequency [Pop]', 'Frequency [Rap]', 'Frequency [Rock]'], axis="columns")
        .loc[:, ['Age','Frequency_[Classical]_num', 'Frequency_[Country]_num','Frequency_[EDM]_num', 'Frequency_[Folk]_num', 'Frequency_[Jazz]_num','Frequency_[Metal]_num', 'Frequency_[Pop]_num', 'Frequency_[Rap]_num','Frequency_[Rock]_num', 'Anxiety', 'Depression', 'Insomnia']]
        .reset_index(drop=True)
    )

    
    # Make sure to return the latest dataframe

    return methodchain2 


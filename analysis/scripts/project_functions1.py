import pandas as pd
#wrapping it in a function
    

def load_and_process(url_or_path_to_csv_file):
    def type_of_music(x):
        '''
        Decides what type of music the responder participated in. If they were a composer, instrumentalist, both, or neither
        '''
        if (x['Instrumentalist']=="Yes") & (x['Composer']=="Yes"):
            return "Both"
        elif x['Instrumentalist']=="Yes": 
            return "Instrumentalist"  
        elif x['Composer']=="Yes":
            return "Composer"
        else:
            return "Neither"
    def standardization(x):
        '''
        returning the standardized value of Hours per day based on the maximum value, standard deviation, and the mean of the dataset
        '''
        return ((x['Hours per day']-3.6030995106035886)/(2.730156903404203)+1)/8.470962736230923*100


    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .dropna()
        .reset_index(drop=True)
)

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
        .assign(
            Overall_mental_health=lambda x: x['Anxiety']*.35+x['Depression']*.35+x['Insomnia']*.2+x['OCD']*.1)
        .assign(
            Music_Participation=lambda x: x.apply(type_of_music, axis="columns"))
        .reset_index(drop=True)
        .assign(
            Hours_per_day_Percentage=lambda x: x.apply(standardization,axis="columns")
        )
        .loc[:, ["Instrumentalist", "Composer", "Hours_per_day_Percentage", "Anxiety", "Depression","Insomnia","OCD", "Music effects","Music_Participation","Overall_mental_health"]]


      )

    # Make sure to return the latest dataframe

    return df2 
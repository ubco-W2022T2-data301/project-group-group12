import pandas as pd
#wrapping it in a function
def load_and_process(url_or_path_to_csv_file):

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
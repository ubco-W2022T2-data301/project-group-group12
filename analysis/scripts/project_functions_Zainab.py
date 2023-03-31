{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "df8149da-b966-4681-bb28-bbe6f25460b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f7c2455e-9d3b-439a-8901-62c08fc6ccb2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process(url_or_path_to_csv_file):\n",
    "\n",
    "    # Method Chain 1 (Load data and deal with missing data)\n",
    "\n",
    "    datasetchain1 = (\n",
    "                pd.read_csv('../data/raw/music_therapy_and_mental_health_survey_results (1).csv') \\\n",
    "                .drop(columns=['Timestamp', 'While working', 'Instrumentalist', 'Composer', 'Fav genre', 'Exploratory', 'Foreign languages', 'BPM', 'Frequency [Classical]', 'Frequency [Country]', 'Frequency [EDM]', 'Frequency [Folk]', 'Frequency [Gospel]', 'Frequency [Hip hop]', 'Frequency [Jazz]', 'Frequency [K pop]', 'Frequency [Latin]', 'Frequency [Lofi]', 'Frequency [Metal]', 'Frequency [Pop]', 'Frequency [R&B]', 'Frequency [Rap]', 'Frequency [Rock]', 'Frequency [Video game music]', 'Music effects', 'Permissions']) \\\n",
    "                .dropna(subset=['Age', 'Primary streaming service']) \n",
    "    )\n",
    "\n",
    "    # Method Chain 2 (Create new columns, drop others, and do processing)\n",
    "\n",
    "    datasetchain2 = (\n",
    "          datasetchain1\n",
    "            .assign(Primary_streaming_service_in_numbers=lambda x: x.apply(Primarystreamingservice, axis=\"columns\")) \\\n",
    "            .assign(Primary_streaming_service_in_numbers_float=lambda x: x['Primary_streaming_service_in_numbers'].astype(float)) \\\n",
    "            .assign(Hours_per_day_percentage=lambda x: x['Hours per day']/24 * 100) \\\n",
    "            .assign(Overall_Mental_Health_out_of_100=lambda x: (x['Anxiety'] + x['Depression'] + x['Insomnia'] + x['OCD'])*2.5) \\\n",
    "            .loc[:, ['Age', 'Primary streaming service', 'Primary_streaming_service_in_numbers', 'Hours_per_day_percentage', 'Anxiety', 'Depression', 'Insomnia', 'OCD', 'Overall_Mental_Health_out_of_100']]\n",
    "    \n",
    "    )\n",
    "\n",
    "    # Make sure to return the latest dataframe\n",
    "\n",
    "    return datasetchain2 "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

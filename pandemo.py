import pandas as pd
import numpy as np
import os


# Proper file path management => base path is current location of script file
CURR_DIRR_PATH = os.path.dirname(os.path.realpath(__file__))
# BASE path joined with the file for reading - csv file assumed to be in the same directory as script
df = pd.read_csv(os.path.join(CURR_DIRR_PATH, 'ruined_automobile_data.csv'))

## NOTE: __file__ is not defined when you're running an interactive session (say, Jupyter Notebook)
## There the current working directory should be where .ipynb file exists, and you'll have to make do with a relative path:
# CURR_DIRR_PATH = ""  # Empty => relative path


# We won't do regexes, but this would be a nifty pattern match for a string that's acceptable e-mail formating
regex_for_matching_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


# From a pre-defined list, we can check if a column value can be found in that list
acceptable_body_style = ['sedan', 'hatchback', 'wagon', 'hardtop']
print(df[df['body-style'].isin(acceptable_body_style)])
# Other useful methods in a similar category: duplicated, isnull


# Common way to create a dataframe from lists of values.
# A dataframe can be created from a dict, where the keys will be considered the columns,
# and each respective list connected to a key will be the column values, forming rows.
fish_names = ["rutger", "pedro", "vilhelmina", "häst"]
weight = [5, 2, 1, 4]
df_fish = pd.DataFrame({'name': fish_names, 'weight': weight})


# Note the difference between DataFrame/Series.str.replace() and DataFrame/Series.replace()
df_fish['name'] = df_fish['name'].str.replace('ä', 'a')
print(df_fish)
# During the Rhode Island data inspection, we used the DataFrame version and replaced field values in the dataframe
# Here we are looking at all the string values in a column of dtype: object (str), and replacing occurences of individual letters,
# not far from the replace string-method in regular Python.


# BASE path joined with the file path for WRITING, index=False excludes the index metadata-column.
# Try with and without the argument and compare the content of the resulting file.
df_fish.to_csv(os.path.join(CURR_DIRR_PATH, 'fish.csv'), index=False)
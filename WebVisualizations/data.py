# Read in a csv file and write out to html
import pandas as pd

# Read the csv file in for weather dashboard
df = pd.read_csv('Resources/cities.csv')

# Get an HTML format of a dataframe by 
# using the DataFrame.to_html() method. 
df.to_html('dframe_generated_data.html', index=False)

# Assign and print
table = df.to_html()
print(table)
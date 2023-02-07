import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_excel('Dataset.xlsx') 

print(df)

# Generate Report
profile = ProfileReport(df)
#profile = ProfileReport(df, minimal=True)
profile.to_file(output_file="dateset.html")


# Importing libraries
import pandas as pd
import nltk
import re
import string

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

csv_file_name = "data_science.csv"

# Downloading DataSet Recommender By NLTK
nltk.download('omw-1.4')

# Read csv file into a pandas dataframe
df = pd.read_csv(csv_file_name)

# Take a look at the first few rows
print("Real CSV Data: \n", df.head(), 'asd', df.columns.to_list())

# Making a list of missing value types
missing_values = ["n/a", "na", "--", " ", ""]
df = pd.read_csv(csv_file_name, na_values=missing_values)


df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)

# WordNetLemmatizer

all_columns = df.columns.to_list()
# New DataFrame
new_df = pd.DataFrame()

all_columns_data = {}
stemmer = WordNetLemmatizer()

for column in all_columns:
    all_columns_data[column] = []
    if df[column].dtypes == 'float64' or df[column].dtypes == 'int64':
        for data in df[column]:
            all_columns_data[column].append(data)
        continue
    for data in df[column]:
        document = re.sub(r'\W', ' ', str(data))
        documents = re.sub(re.escape(string.punctuation), ' ', document)
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
        document = re.sub(r'\s+', ' ', document, flags=re.I)
        document = re.sub(r'^b\s+', ' ', document)
        document = document.lower()
        # lemitization
        document = document.split()
        document = [stemmer.lemmatize(word) for word in document]
        document = ' '.join(document)
        document = [word for word in document.split(
        ) if word not in stopwords.words("english")]
        document = ' '.join(document)
        all_columns_data[column].append(document)


for index, column_name in enumerate(all_columns_data.keys()):
    new_df.insert(index, column_name, all_columns_data[column_name])

print('Original:\n', df)
print('After Lemmatizer\n', new_df)

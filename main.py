# Importing libraries
import pandas as pd
import nltk
import re
import string

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Downloading
nltk.download('omw-1.4')


# Read csv file into a pandas dataframe
df = pd.read_csv("property data.csv")

# Take a look at the first few rows
print("Real CSV Data: \n", df.head(), 'asd', df.columns.to_list())

# Making a list of missing value types
missing_values = ["n/a", "na", "--", " ", ""]
df = pd.read_csv("property data.csv", na_values=missing_values)


df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)

# WordNetLemmatizer

all_columns = df.columns.to_list()
# New DataFrame
new_df = pd.DataFrame()

all_columns_data = {}
stemmer = WordNetLemmatizer()

for column in all_columns:
    all_columns_data[column] = []
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


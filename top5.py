import csv
import pandas as pd
from collections import Counter


data = []
with open("imdb_cast/output.csv", encoding="utf-8", newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# Initialize pandas dataframe to get value frequencies
df = pd.DataFrame(data=data, columns=['name'])
count = df.name.value_counts().to_dict()

# Use counter to get top 5 frequent values
k = Counter(count)
five_highest = k.most_common(5)

# Move top 5 actors/actresses to empty list 
top5_cast_members = []
for i in five_highest:
    top5_cast_members.append(i[0])

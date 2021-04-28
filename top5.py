import csv
import pandas as pd
from collections import Counter


data = []
with open("imdb_cast/output.csv", encoding="utf-8", newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# Initialize pandas dataframe to get value frequencies
# and transfer data into python dict where keys are names 
# and values are the frequency
df = pd.DataFrame(data=data, columns=['name'])
count = df.name.value_counts().to_dict()

# Use counter to get top 5 
k = Counter(count)
five_highest = k.most_common(5)

# Move top 5 actors/actresses to empty list 
top5_cast_members = []
for i in five_highest:
    top5_cast_members.append(i[0])

# Open the upload file and write the list content 
upload_file = open('upload/to_upload.csv','w')
writer = csv.writer(upload_file, dialect='excel')

for cast_member in top5_cast_members:
    writer.writerow([cast_member])
print(f"Top 5 cast members are: {top5_cast_members}\n...\nWriting into drive upload file now")
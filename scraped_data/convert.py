import json

# Open and read the JSON file
with open('arcane_scribe.json', 'r', encoding='utf-8') as file:
    data1 = json.load(file)
    arcane_scribe_comments = []
    for row in data1:
        arcane_scribe_comments.append(row['commentText'])

with open('golden_frog_inn.json', 'r', encoding='utf-8') as file:
    data2 = json.load(file)
    golden_frog_comments = []
    for row in data2:
        golden_frog_comments.append(row['commentText'])

with open('output1.txt', 'w') as filehandle:
    json.dump(arcane_scribe_comments, filehandle)

with open('output2.txt', 'w') as filehandle:
    json.dump(golden_frog_comments, filehandle)
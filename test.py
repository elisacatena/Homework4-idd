import random
import os
import json

myPath = "C:/Users/MariaDeDomenico/OneDrive - Lobra S.r.l/Desktop/file hw4/jsons/"
filesName = os.listdir(myPath)
visited_files = []

for i in range(0, 300):

    file_number = random.randint(0, len(filesName)-1)
    while file_number in visited_files :
        file_number = random.randint(0, len(filesName)-1)
    
    visited_files.append(file_number)
    json_file = open(myPath+filesName[i]).read()

    json_data = json.load(json_file)

    






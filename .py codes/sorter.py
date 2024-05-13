import pandas as pd
import os

input_texts = []
target_texts = []
with open('chatbot dataset.txt') as f:
    lines = f.read().split('\n')
for line in lines[: min(600, len(lines) - 1)]:
    input_text = line.split('\t')[0]
    target_text = line.split('\t')[1]
    input_texts.append(input_text)
    target_texts.append(target_text)

##converting the list in pandas dataframe since input_text,target_text are both are type of list
zippedList =  list(zip(input_texts, target_texts))
lines = pd.DataFrame(zippedList, columns = ['input' , 'output']) 
lines = pd.DataFrame(lines)
lines.to_csv('chatdataset.csv')
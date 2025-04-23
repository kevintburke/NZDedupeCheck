"""CHECKS NZ DEDUPE REPORT (SORTED!) FOR SIMILARITY BETWEEN RECORDS WITH MATCHING OCLC #s IN IDENTIFIER COLUMN"""
import pandas as pd
from fuzzywuzzy import fuzz
import numpy as np
import datetime
from tkinter import filedialog
import time

COMPARISON_FIELDS = ['Title','Publication Date','Language Of Cataloging','Author','ISBN (Normalized)','Edition','Publisher']

def compare_fields(field, row1, row2):
    sim = fuzz.WRatio(str(row1.get(f'{field}')), str(row2.get(f'{field}')))
    return sim

def similarity(i, j, df):
    #Compare row1 at identifier to row2 at identifier
    row1 = df.iloc[i]
    row2 = df.iloc[j]
    similarities = []
    # print(row1, row2)
    if row1.get('Identifier') == row2.get('Identifier'):
        print(f'MATCH: Row {i} and Row {j}')
        for field in COMPARISON_FIELDS:
            similarities.append(compare_fields(field, row1, row2))
        print(similarities)
        sim = np.mean(similarities)
        df.loc[df.index[i], 'Similarity'] = sim
        df.loc[df.index[j], 'Similarity'] = sim
    else:
        print(f'MISMATCH: Row {i} and Row {j}')

def main():
    #Use filedialog to open file for processing
    print("Please select an NZ Dedupe Report (in CSV) to process:")
    time.sleep(1.5)
    file = filedialog.askopenfilename()
    with open(file, 'r', encoding='utf-8') as file:
        df = pd.read_csv(file)
    df.insert(17,'Similarity','0')
    #Call similarity comparison on each row
    for i in range(len(df)-1):
        j = i+1
        sim = similarity(i, j, df)
    timestamp = datetime.datetime.today().strftime('%m%d%H%M')
    df.to_csv(f'output{timestamp}.csv',index=False)
    print(f'\nOutput saved to output{timestamp}.csv')

if __name__ == "__main__":
    main()
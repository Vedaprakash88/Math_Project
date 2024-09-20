import pandas as pd 
  
for x in range(6):
    tsv_file=f'D:\\6. STUDY MATERIAL\\CSE\Projects\\Python\\Data_Sets\\data{x+1}.tsv'
    csv_file=f'D:\\6. STUDY MATERIAL\\CSE\Projects\\Python\\Data_Sets\\data{x+1}.csv'
  
    # readinag given tsv file
    csv_table=pd.read_table(tsv_file,sep='\t')
  
    # converting tsv file into csv
    csv_table.to_csv(csv_file,index=False)
  
    # output
    print("Successfully made csv file")
import numpy as np
dt = np.loadtxt('D:\\6. STUDY MATERIAL\\CSE\Projects\\Python\\Data_Sets\\data4.txt', delimiter='\t', skiprows=1, dtype = 'str', encoding='utf-8')


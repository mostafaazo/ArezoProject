#%%
import os
import pandas as pd
import xlrd
import openpyxl

cwd = os.path.abspath("C:/Users/MostafaAzo/Desktop/تفکیک")
# files = os.listdir(cwd)

files = list()
for (dirpath, dirnames, filenames) in os.walk(cwd):
    files += [os.path.join(dirpath, file) for file in filenames]

df = pd.DataFrame()

i=0

for file in files:
     if file.endswith('.xlsx') and ("$" not in file):
         print(file)


         f= pd.read_excel(file, nrows=6000, usecols='A:I')
         f.columns = ["ردیف", "استان", "شهرثبت نام", "نام", "نام خانوادگی", "شماره نظام", "گروه", "کد ملی", "تخصص"]

         f["fileName"] = file.split(os.sep)[-1]
         df = df.append(f, ignore_index=True)

         print(i)
         i= i + 1

df.head()

#$$



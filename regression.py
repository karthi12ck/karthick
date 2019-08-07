# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 09:34:15 2019

@author: Training85
"""

#regression

data=pd.read_excel(r'C:\karthick\kaggle datasets\Property Price\Dataset.xlsx')
data_without_null=data.dropna(axis=0,subset=[['floor','max_floor','material','build_year','num_room']],thresh=1).count()
target=data.iloc[:,291:]
target=data_without_null[:,291:]

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
x_new=SelectKBest(chi2,k=20).fit_transform(train_data,target)
 macro=macro.iloc[:-1,:]
new_data=pd.merge(data,macro,how='inner',left_on='timestamp',right_on='timestamp')
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt 
from datetime import datetime
import datetime 
import time 
import collections 
import pandas as pd
import numpy as np
from matplotlib import colors
from matplotlib import cm 
import os 
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point


# In[2]:


df = pd.read_csv('bierstadter.csv')


# In[3]:


# Convert the timestamp column to datetime objects
df['Datetime'] = pd.to_datetime(df['Timestamp'], unit='ms')

# Set the starting date to November 22, 2022
start_date = pd.to_datetime('2022-11-22')

# Add the starting date to the datetime objects
df['Datetime'] = start_date + (df['Datetime'] - df['Datetime'].min())


# Print the resulting DataFrame
print(df)


# In[4]:


df = df.loc[df['Datetime'].dt.date != pd.to_datetime('2022-11-22').date()]
#df


# In[5]:


bss=pd.read_excel('bss.xlsx')
#bss


# In[6]:


df[['X', 'Y']] = df[['X', 'Y']].div(1000)


# In[7]:


import pandas as pd


for i, row in df.iterrows():
    x, y = row['X'], row['Y']
    for j, row2 in bss.iterrows():
        if row2['minX'] <= x <= row2['maxX'] and row2['minY'] <= y <= row2['maxY']:
            df.loc[i, 'area'] = row2['areasPermanentId']
            break


# In[8]:


df['area'].fillna(111, inplace=True)
df


# In[70]:


df['idTblLoc'] = 3


# In[71]:


start_time = '2023-01-30'
end_time = '2023-01-31'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
#print(df_filtered)


# In[72]:


df_filtered


# In[73]:


df_filtered.to_csv('bss1.csv', index=False)


# In[50]:





# In[ ]:





# In[74]:


start_time = '2023-01-31'
end_time = '2023-02-01'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[75]:


df_filtered.to_csv('bss2.csv', index=False)


# In[76]:


start_time = '2023-02-01'
end_time = '2023-02-02'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[77]:


df_filtered.to_csv('bss3.csv', index=False)


# In[78]:


start_time = '2023-02-02'
end_time = '2023-02-03'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[79]:


df_filtered.to_csv('bss4.csv', index=False)


# In[80]:


start_time = '2023-02-03'
end_time = '2023-02-04'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[81]:


df_filtered.to_csv('bss5.csv', index=False)


# In[82]:


start_time = '2023-02-04'
end_time = '2023-02-05'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[83]:


df_filtered.to_csv('bss6.csv', index=False)


# In[ ]:





# In[84]:


start_time = '2023-02-05'
end_time = '2023-02-06'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[85]:


df_filtered.to_csv('bss7.csv', index=False)


# In[86]:


start_time = '2023-02-06'
end_time = '2023-02-07'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[87]:


df_filtered.to_csv('bss8.csv', index=False)


# In[88]:


start_time = '2023-02-07'
end_time = '2023-02-08'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[89]:


df_filtered.to_csv('bss9.csv', index=False)


# In[90]:


start_time = '2023-02-08'
end_time = '2023-02-09'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[91]:


df_filtered.to_csv('bss10.csv', index=False)


# In[92]:


start_time = '2023-02-09'
end_time = '2023-02-10'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[93]:


df_filtered.to_csv('bss11.csv', index=False)


# In[94]:


start_time = '2023-02-10'
end_time = '2023-02-11'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[95]:


df_filtered.to_csv('bss12.csv', index=False)


# In[96]:


start_time = '2023-02-11'
end_time = '2023-02-12'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[97]:


df_filtered.to_csv('bss13.csv', index=False)


# In[98]:


start_time = '2023-02-12'
end_time = '2023-02-13'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[99]:


df_filtered.to_csv('bss14.csv', index=False)


# In[100]:


start_time = '2023-02-13'
end_time = '2023-02-14'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[ ]:





# In[101]:


df_filtered.to_csv('bss15.csv', index=False)


# In[102]:


start_time = '2023-02-14'
end_time = '2023-02-15'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[103]:


df_filtered.to_csv('bss16.csv', index=False)


# In[104]:


start_time = '2023-02-15'
end_time = '2023-02-16'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[105]:


df_filtered.to_csv('bss17.csv', index=False)


# In[106]:


start_time = '2023-02-16'
end_time = '2023-02-17'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[107]:


df_filtered.to_csv('bss18.csv', index=False)


# In[108]:


start_time = '2023-02-17'
end_time = '2023-02-18'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[109]:


df_filtered.to_csv('bss19.csv', index=False)


# In[110]:


start_time = '2023-02-18'
end_time = '2023-02-19'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[111]:


df_filtered.to_csv('bss20.csv', index=False)


# In[118]:


start_time = '2023-02-13'
end_time = '2023-02-14'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364 and trigger == True:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[119]:


df_filtered.to_csv('testbss1.csv', index=False)


# In[115]:


start_time = '2023-02-15'
end_time = '2023-02-16'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False

for i, row in df_filtered.iterrows():

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364 and trigger == True:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[116]:


df_filtered.to_csv('testbss2.csv', index=False)


# In[121]:


start_time = '2023-02-15'
end_time = '2023-02-16'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

df_filtered['path_id'] = 1
pathid_counter = 1
trigger = False
prev_device_id = None

for i, row in df_filtered.iterrows():
    
    curr_device_id = row['DeviceId']

    if curr_device_id != prev_device_id:
        pathid_counter = 1
        trigger = False

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364 and trigger == True:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
    
    prev_device_id = curr_device_id

print(df_filtered)


# In[122]:


df_filtered.to_csv('testbss3.csv', index=False)


# In[123]:


start_time = '2023-02-17'
end_time = '2023-02-18'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'])

pathid_counters = {}
for device_id in df_filtered['DeviceId'].unique():
    pathid_counters[device_id] = 1

df_filtered['path_id'] = 1

for i, row in df_filtered.iterrows():

    device_id = row['DeviceId']
    pathid_counter = pathid_counters[device_id]

    if row['area'] == 1363:
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counters[device_id] += 1
        df_filtered.loc[i, 'path_id'] = pathid_counters[device_id]
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


# In[124]:


df_filtered.to_csv('testbss4.csv', index=False)


# In[125]:


start_time = '2023-02-17'
end_time = '2023-02-18'

df_filtered = df[(df['Datetime'] >= start_time) & (df['Datetime'] <= end_time)].reset_index(drop=True)

df_filtered = df_filtered.sort_values(by=['DeviceId', 'Datetime'], ascending=[True, True])

df_filtered['path_id'] = 1
pathid_counter = 1
device_id = None
trigger = False

for i, row in df_filtered.iterrows():

    if row['DeviceId'] != device_id:
        device_id = row['DeviceId']
        pathid_counter = 1
        trigger = False

    if row['area'] == 1363:
        trigger = True
        df_filtered.loc[i, 'path_id'] = pathid_counter
    elif row['area'] == 1364:
        pathid_counter += 1
        trigger = False
        df_filtered.loc[i, 'path_id'] = pathid_counter
    else:
        df_filtered.loc[i, 'path_id'] = pathid_counter
        
print(df_filtered)


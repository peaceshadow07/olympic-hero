# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)


data['Better_Event'] = np.where(data['Total_Summer']>=data['Total_Winter'],'Summer','Winter')
data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])
print(data.head())
better_event = data['Better_Event'].value_counts()
for key,value in better_event.items():
    if value==better_event.max():
        better_event=key
        break
print(better_event)





top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries.drop(top_countries.index[146],inplace=True)
def top_ten(top_countries,Column):
    return list(top_countries.nlargest(10,Column)['Country_Name'])

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')
common = list(set(top_10).intersection(set(top_10_summer)).intersection(set(top_10_winter)))
# common = pd.merge(common,top_10_winter,how='inner')



top_df = data[data['Country_Name'].isin(top_10)]
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]

fig,(ax_1,ax_2,ax_3) = plt.subplots(3,1,figsize=(15,10))
top_df['Total_Medals'].value_counts().plot(kind='bar',ax = ax_1)
summer_df['Total_Summer'].value_counts().plot(kind='bar',ax = ax_2)
winter_df['Total_Winter'].value_counts().plot(kind='bar',ax = ax_3)
ax_1.set_title('Overall Top Performer')

ax_2.set_title('Summer Top Performer')
ax_3.set_title('Winter Top  Performer')




summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']

summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = list(summer_df['Country_Name'][summer_df['Golden_Ratio']==summer_max_ratio])[0]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']

winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = list(winter_df['Country_Name'][winter_df['Golden_Ratio']==winter_max_ratio])[0]

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']

top_max_ratio = top_df['Golden_Ratio'].max()

top_country_gold = list(top_df['Country_Name'][top_df['Golden_Ratio']==top_max_ratio])[0]



data_1 = data.drop(data.index[146])
data_1['Total_Points'] = data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total']
most_points = data_1['Total_Points'].max()
best_country = list(data_1['Country_Name'][data_1['Total_Points']==most_points])[0]


best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot(kind='bar',stacked=True)
plt.xlabel(best['Country_Name'])
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)



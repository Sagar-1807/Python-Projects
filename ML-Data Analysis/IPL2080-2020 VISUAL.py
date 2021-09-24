#VISUALIZATON
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

data=pd.read_csv('D:\Study\Data Science\Data sets\IPL Matches 2008-2020.csv')
# print(data.head(-5))#last & 1st 5 rows
# print(data.info())

#now method colmn has lot of null value so remove it
# axis=0 means row,1 =colmn,inplace means update data
data.drop(['method'],axis=1,inplace=True)
# print(data.info())

#-----------most winner team------------------------
temp=pd.DataFrame({'Most Winner Team':data['winner']})
win_count=temp.value_counts()
# print(win_count)
w_key=[i[0] for i in win_count.keys()]
# print(w_key)
# a,b=plt.subplots(figsize=(12,6))
# b=plt.pie(x=win_count,autopct='%0.1f%%',labels=w_key)
#plt.title("most ipl winner",fontsize=18)
#plt.show()

#--------------------Most winer in eliminator
#
# sb.countplot(data['winner'][data['eliminator'] == 'Y'],data=data)
# plt.title("Most winner in eliminator",fontsize=14)
# plt.xticks(rotation=45)
# plt.show()
#

#-------------------------------EDA------------------
# TOSS DECISION -

team=data['toss_winner'].unique()
# print(team)

decision=pd.DataFrame([],columns=['Toss winner','Bat/Field','Times'])

for id,result in enumerate(team):
    win_bat=data[(data['toss_winner']==result) & (data['toss_decision']=='bat')]
    win_field=data[(data['toss_winner']==result) & (data['toss_decision']=='field')]
#append  in list

    decision=decision.append({'Toss winner':result,
            'Bat/Field':'bat','Times':win_bat['toss_winner'].count()},ignore_index=True)
    decision = decision.append({'Toss winner':result,
            'Bat/Field':'field','Times':win_bat['toss_winner'].count()},ignore_index=True)

#print(decision)

#--------graph of toss decision
#
#sb.catplot(y='Toss winner',x='Times',hue='Bat/Field',kind='bar',
#            data=decision,height=3,aspect=2)
#plt.title('Toss winner graph')
#plt.xticks(rotation=90)
#plt.ylabel('[Team]')
#plt.xlabel('Toss decision')
#plt.show()

#--------graph of place
#
# sb.barplot(x=data['venue'].value_counts().head(8).values,
#     y=data['venue'].value_counts().head(8).index,data=data)
# plt.title('Famous place')
# plt.xlabel('Place freq.')
# plt.ylabel('Place')
# plt.show()

#-------------------------- Top umpire
sb.barplot(x=data['umpire1'].value_counts().head(6).index,
    y=data['umpire1'].value_counts().head(6).values,data=data)
plt.xlabel('umpire name')
plt.ylabel('Matches played')
plt.title('Top Umpire')
plt.show()
















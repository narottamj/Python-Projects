import pandas as pd
import numpy as np

df = pd.read_csv("LaCasaDePapel_Trivia.csv")
df['YesNo'] = np.where(df['Correct']=='Y',round(1),round(0))
print(df.columns.tolist())
df = df.pivot_table(index=['Time', 'Topic', 'Location', 'Measure', 'CustomerID', 'DateReported', 'PossiblePoints'], columns = 'Question', values = 'YesNo', fill_value=0, aggfunc=np.sum).reset_index()
df.index.name = df.columns.name = None
df = df.fillna(int(0))
df['RawScore'] = df.loc[:,'How did Moscow die?':'With whom does Berlin get married?'].sum(axis=1)
df['PercentScore']=round((df['RawScore']/df['PossiblePoints'])*100).astype(int)
print(df)
df.to_csv('LaCasaDePapel_Trivia_Finished.csv')
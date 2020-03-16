
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import yfinance as yf

--------------------------------------------------------
�����κ��������΢��tyrant100
--------------------------------------------------------

#���ݻ�ȡ
df_data = yf.download('NVDA', start='2015-01-02', end='2020-01-01', progress=False) #progress�ǽ�����ʾ������ùر�

#���ݴ���
df = df_data[['Adj Close']] #����Ҫ������[]��������һ��series������df
df['s_r'] = df/df.shift(1)-1
df.rename(columns={'Adj Close':'adj_close'},inplace=True)
df_dates = pd.DataFrame(index=pd.date_range(start='2015-1-1', end='2019-12-31'))
df = df_dates.join(df)
df=df.fillna(method='ffill').asfreq('M')
cpi = pd.read_excel('cpi_data.xlsx')
cpi = cpi[:, 1:].flatten()
df['cpi'] = cpi
df['inf_rate'] = df.cpi.pct_change()
df['r_r']=(df.s_r+1)/(df.inf_rate+1)-1

#���ݿ��ӻ�
plt.style.use('ggplot')
fig, ax = plt.subplots(4, 1, figsize=(12, 10), sharex=True)
df.adj_close.plot(ax=ax[0])
ax[0].set(title = 'Nvidia data analysis', ylabel = 'Stock price')
df.s_r.plot(ax=ax[1])
ax[1].set(ylabel = 'Simple returns')
df.inf_rate.plot(ax=ax[2])
ax[2].set(ylabel = 'Inflation rate')
df.r_r.plot(ax=ax[3])
ax[3].set(xlabel = 'Date', ylabel = 'Real Rate of Returns')

'
import pandas as pd
from WindPy import *
from sqlalchemy import create_engine
import datetime,time

w.start()

InitDay = '2019-01-05'
EndDay = '2019-01-09'
#w.wsd('090007.ib','CLOSE',InitDay,EndDay,'Priceadj=f;tradingcalendar=nib')

wsd_data = w.wsd('600000.SH','pre_settle,open,high,low,close,settle',InitDay,EndDay)
insertdata = pd.DataFrame()
time_data = wsd_data.Times
print(time_data)

insertdata['daying'] = time_data
insertdata['presettle'] = wsd_data.Data[0]
insertdata['open'] = wsd_data.Data[1]
insertdata['high'] = wsd_data.Data[2]
insertdata['low'] = wsd_data.Data[3]
insertdata['close'] = wsd_data.Data[4]
insertdata['settle'] = wsd_data.Data[5]
engine = create_engine('mysql+pymysql://root:123456@localhost/tao?charset=utf8mb4')
insertdata.to_sql('windpy',engine,if_exists='append',index=False)
print(InitDay)

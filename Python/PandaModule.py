import pandas as pd

#blank seies
#s=pd.series();

#Series with values
#s=pd.Series([32,54,1,90]);

#any dataType
#s=pd.Series(['p','k','r','s'])

#Series with values and index
#s=pd.Series(['p','k','r','s'],index=[101,102,103,104])


s=pd.Series([101,102,103,104],index=['p','k','r','s'])
#index for search
print(s['r'])
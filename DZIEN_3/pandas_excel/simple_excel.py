import pandas as pd
import xlsxwriter

df = pd.DataFrame({'Dane':[10,12,34,64,256,63,357,424,36,88,325,897,543,6,785,223]})

writer = pd.ExcelWriter('pandas_data.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='ramka')
writer._save()

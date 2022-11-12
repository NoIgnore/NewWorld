import pandas as pd
import os
import numpy as np 
path = "C:\\Users\\12091\\Desktop"
deal_level_data=pd.read_csv(path + os.sep + 'deal_level_data.csv')
quarter_level_data=pd.read_csv(path + os.sep + 'quarter_level_data.csv')
deal_level_data.sample(5)
for index, col in enumerate(deal_level_data.columns): 
    print(index, col) 
quarter_level_data.head(26)
for col in quarter_level_data.columns: 
    print(col) 
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

my_quarter_level_col = []
for col in deal_level_data.columns: 
    if not hasNumbers(col) and "Acq_" not in col:
        my_quarter_level_col.append(col)
        print(col) 
#print(len(my_quarter_level_col)) 
my_quarter_level_data = ['Deal_Number', 'Date_Announced', 'Year_Announced', 'Acquirer_Name_clean', 
                         'Acquirer_Primary_SIC', 'Acquirer_State_abbr', 'Acquirer_CUSIP', 
                         'Acquirer_Ticker', 'Target_Name_clean', 'Target_Primary_SIC', 'Target_State_abbr',
                         'Target_CUSIP', 'Target_Ticker', 'Attitude', 'quarter_to_the_event_date',
                         'quarter', 'Com_Net_Charge_Off', 'Com_Insider_Loan', 'Com_NIE', 'Com_NII',
                         'Com_NIM', 'Com_ROA', 'Com_Total_Assets', 'Com_AvgSalary', 'Com_EmployNum',
                         'Com_TtlSalary', 'Com_AvgSalary_log', 'Com_EmployNum_log', 'Com_TtlSalary_log',
                         'Tar_Net_Charge_Off', 'Tar_Insider_Loan', 'Tar_NIE', 'Tar_NII', 'Tar_NIM', 
                         'Tar_ROA', 'Tar_AvgSalary', 'Tar_EmployNum', 'Tar_TtlSalary', 'Tar_Total_Assets',
                         'Tar_AvgSalary_log', 'Tar_EmployNum_log', 'Tar_TtlSalary_log']

my_quarter_level_data = pd.DataFrame(columns=my_quarter_level_data)
quarter_date_string = ['__12', '__11', '__10', '__9', '__8', '__7', '__6', '__5', '__4', '__3', '__2', "__1",
                '', '_1', '_2', '_3', '_4', '_5', '_6', '_7', '_8', '_9', '_10', '_11', "_12"]

quarter_date_number = [-12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1,
                0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

quarter_level_col = ['quarter', 'Tar_Net_Charge_Off', 'Tar_Insider_Loan', 'Tar_NIE', 'Tar_NII', 'Tar_NIM', 'Tar_ROA', 
                     'Tar_AvgSalary', 'Tar_EmployNum', 'Tar_TtlSalary', 'Tar_Total_Assets', 'Com_Net_Charge_Off', 
                     'Com_Insider_Loan', 'Com_NIE', 'Com_NII', 'Com_NIM', 'Com_ROA', 'Com_Total_Assets', 'Com_AvgSalary',
                     'Com_EmployNum', 'Com_TtlSalary', 'Com_AvgSalary_log', 'Com_EmployNum_log', 'Com_TtlSalary_log',
                     'Tar_AvgSalary_log', 'Tar_EmployNum_log', 'Tar_TtlSalary_log']

count = 0 
for index, row in deal_level_data.iterrows():
    for quarter in range(25):
        my_quarter_level_data.loc[count] = row[0:14]
        my_quarter_level_data.at[quarter, 'quarter_to_the_event_date'] = quarter_date_number[quarter]
        for column in quarter_level_col:
            my_quarter_level_data.at[count, column] = row[column + quarter_date_string[quarter]]
        count += 1
    if index == 3117:
        break
my_quarter_level_data.to_csv('C:/Users/13538/OneDrive - connect.hku.hk/桌面\HKU LESSON\mfin7033/2022 Fall MFIN7033(1)/2022 Fall MFIN7033/2022 Fall Projects/Data transformation/data/my_quarter_level_data.csv')



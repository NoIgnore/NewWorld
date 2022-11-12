import pandas as pd
import os
from concurrent.futures import Future, ProcessPoolExecutor
import time

path = "C:\\Users\\12091\\Desktop\\NewWorld\\Python\\Data"
deal_level_data = pd.read_csv(path + os.sep + 'deal_level_data.csv')
quarter_level_data = pd.read_csv(path + os.sep + 'quarter_level_data.csv')
deal_level_data.sample(5)

for index, col in enumerate(deal_level_data.columns):
    #print(index, col)
    pass

quarter_level_data.head(26)
for col in quarter_level_data.columns:
    #print(col)
    pass

my_quarter_level_col = []


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


for col in deal_level_data.columns:
    if not hasNumbers(col) and "Acq_" not in col:
        my_quarter_level_col.append(col)
        #print(col)

my_quarter_level_data_0 = [
    'Deal_Number', 'Date_Announced', 'Year_Announced', 'Acquirer_Name_clean',
    'Acquirer_Primary_SIC', 'Acquirer_State_abbr', 'Acquirer_CUSIP',
    'Acquirer_Ticker', 'Target_Name_clean', 'Target_Primary_SIC',
    'Target_State_abbr', 'Target_CUSIP', 'Target_Ticker', 'Attitude',
    'quarter_to_the_event_date', 'quarter', 'Com_Net_Charge_Off',
    'Com_Insider_Loan', 'Com_NIE', 'Com_NII', 'Com_NIM', 'Com_ROA',
    'Com_Total_Assets', 'Com_AvgSalary', 'Com_EmployNum', 'Com_TtlSalary',
    'Com_AvgSalary_log', 'Com_EmployNum_log', 'Com_TtlSalary_log',
    'Tar_Net_Charge_Off', 'Tar_Insider_Loan', 'Tar_NIE', 'Tar_NII', 'Tar_NIM',
    'Tar_ROA', 'Tar_AvgSalary', 'Tar_EmployNum', 'Tar_TtlSalary',
    'Tar_Total_Assets', 'Tar_AvgSalary_log', 'Tar_EmployNum_log',
    'Tar_TtlSalary_log'
]

my_quarter_level_data = pd.DataFrame(columns=my_quarter_level_data_0)
quarter_date_string = [
    '__12', '__11', '__10', '__9', '__8', '__7', '__6', '__5', '__4', '__3',
    '__2', "__1", '', '_1', '_2', '_3', '_4', '_5', '_6', '_7', '_8', '_9',
    '_10', '_11', "_12"
]

quarter_date_number = [
    -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7,
    8, 9, 10, 11, 12
]

quarter_level_col = [
    'quarter', 'Tar_Net_Charge_Off', 'Tar_Insider_Loan', 'Tar_NIE', 'Tar_NII',
    'Tar_NIM', 'Tar_ROA', 'Tar_AvgSalary', 'Tar_EmployNum', 'Tar_TtlSalary',
    'Tar_Total_Assets', 'Com_Net_Charge_Off', 'Com_Insider_Loan', 'Com_NIE',
    'Com_NII', 'Com_NIM', 'Com_ROA', 'Com_Total_Assets', 'Com_AvgSalary',
    'Com_EmployNum', 'Com_TtlSalary', 'Com_AvgSalary_log', 'Com_EmployNum_log',
    'Com_TtlSalary_log', 'Tar_AvgSalary_log', 'Tar_EmployNum_log',
    'Tar_TtlSalary_log'
]


def CreateRows(row1, levelData1, mainIndex1):
    for index in range(25):
        levelData1.loc[index] = row1[0:14]
        levelData1.at[index,
                      'quarter_to_the_event_date'] = quarter_date_number[index]
        for column in quarter_level_col:
            levelData1.at[index,
                          column] = row1[column + quarter_date_string[index]]
    return mainIndex1, levelData1


if __name__ == '__main__':
    work_requests = []
    time_start = time.time()
    with ProcessPoolExecutor(max_workers=8) as executor:
        for index, row in deal_level_data.iterrows():
            levelData = pd.DataFrame(columns=my_quarter_level_data_0)
            f: Future = executor.submit(CreateRows,
                                        row1=row,
                                        levelData1=levelData,
                                        mainIndex1=index)
            work_requests.append(f)
            if index == 3117:
                break

    myDiction = {}

    for f in work_requests:
        k, v = f.result()
        myDiction[k] = v

    my_quarter_level_data = myDiction[0]
    for key in myDiction:
        if key != 0:
            my_quarter_level_data = pd.concat(
                [my_quarter_level_data, myDiction[key]], ignore_index=True)
    my_quarter_level_data.to_csv(
        "C:\\Users\\12091\\Desktop\\NewWorld\\Python\\Data\\result.csv")
    time_end = time.time()
    time_sum = time_end - time_start
    print(time_sum)

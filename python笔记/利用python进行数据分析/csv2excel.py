
import pandas as pd

def csv2excel(file_name):
    df = pd.read_csv(file_name+'.csv')
    df.to_excel(file_name+'.xlsx', index=None)
    
if __name__ == '__main__':
    file_name = input('please enter file_name:')
    file_name = file_name.strip()
    csv2excel(file_name)

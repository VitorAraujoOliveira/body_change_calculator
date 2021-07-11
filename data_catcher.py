import pandas as pd




class data_catcher:
    def get_yearly_data(year):
        csv_file = 'yearly/yearly_body_data_'+str(year)+'.csv'
        df = pd.read_csv(csv_file,sep=';')
        return df
    
    def get_monthly_data(folder_name,month_name):
        csv_file = folder_name + "/measurements_"+month_name+".csv"
        df = pd.read_csv(csv_file,sep=';')
        return df

    def get_incremental_days_year(year):
        csv_file = 'yearly/yearly_body_data_'+str(year)+'.csv'
        df = pd.read_csv(csv_file,sep=';')
        incremental_days = []
        i = 0
        for i in  range(len(df)):
            incremental_days.append(i+1)
        
        return incremental_days

    def get_first_last_days_year(year):
        csv_file = 'yearly/yearly_body_data_'+str(year)+'.csv'
        df = pd.read_csv(csv_file,sep=';')

        return [df['Date'][0], df['Date'][len(df)-1]] 
        
    def get_first_last_days_month(folder_name,month_name):
        csv_file = folder_name + "/measurements_"+month_name+".csv"
        df = pd.read_csv(csv_file,sep=';')
        return [df['Date'][0], df['Date'][len(df)-1]] 


    def get_last_measurement_line(year):
        csv_file = 'yearly/yearly_body_data_'+str(year)+'.csv'
        df = pd.read_csv(csv_file,sep=';')
        
        return df.tail(1)


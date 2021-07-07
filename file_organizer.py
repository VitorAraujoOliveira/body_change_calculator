
from calendar import month
import pandas as pd
import csv

from pathlib import Path
import os

class file_organizer:
    def open_config_file():
        with open('config.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            file_content_dict = {}

            for i in csv_reader:
                file_content_dict.update({i[0]: i[1]})
        csv_file.close


        return file_content_dict

    # =============== YEARLY =================================================
    def open_yearly_file(year):
        path_to_file = 'yearly/yearly_body_data_'+str(year)+'.csv'
        if not os.path.exists(path_to_file):
            open(path_to_file, 'w').close()

        first_line = (open(path_to_file).readline())
        print('FIRST LINE: '+open(path_to_file).readline())
        if first_line == '':
            f = open(path_to_file, "a")
            f.write("Date;Weight(kg);Waist(cm);Belly(cm);Thighs(cm);Biceps(cm);Body Fat(mm);BMI;BMI class;")
            f.close()

    def save_yearly_data(data,year):
        path_to_file = 'yearly/yearly_body_data_'+str(year)+'.csv'
        f = open(path_to_file,'a')
        f.write('\n'+data)
        f.close

    # =============== MONTHLY =================================================
    def open_monthly_file(folder_name,month_name):
        path_to_file = folder_name + "/measurements_"+month_name+".csv"

        if not os.path.exists(path_to_file):
            open(path_to_file, 'w').close()

        first_line = (open(path_to_file).readline())
        if first_line == '':
            f = open(path_to_file, "a")
            f.write("Date;Weight(kg);Waist(cm);Belly(cm);Thighs(cm);Biceps(cm);Body Fat(mm);BMI;BMI class;")
            f.close()

    def save_monthly_data(data,folder_name,month_name):
        path_to_file = folder_name + "/measurements_"+month_name+".csv"
        f = open(path_to_file,'a')
        f.write('\n'+data)
        f.close



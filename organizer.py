from calendar import month
from datetime import date
import sys
import os
import date_calculator
from pathlib import Path




class organizer:
    def monthly_folder_organizer():
        # (01/2021) january 

        month = date_calculator.date_calculator.get_current_month()
        year = date_calculator.date_calculator.get_current_year()
        month_name = date_calculator.date_calculator.get_month_name()

        folder_name = "monthly/("+str(month)+"-"+str(year)+") "+str(month_name)


        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)

        return folder_name
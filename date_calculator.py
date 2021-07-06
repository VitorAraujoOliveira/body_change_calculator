import datetime 
import calendar



class date_calculator:
    def get_last_day_month():
        any_date = datetime.datetime.now().date()
        
        next_month = any_date.replace(day=28) + datetime.timedelta(days=4)
        
        last_day_of_month = next_month - datetime.timedelta(days=next_month.day)
        
        return(last_day_of_month.day)

    def get_today_date():
        today = datetime.datetime.now().date()
        today = today.strftime("%d/%m/%Y")
        return(today)
    
    def get_today_day():
        today_day = datetime.datetime.now().date().day

        return(today_day)

    def get_current_month():
        current_month = datetime.datetime.now().date().month

        return(current_month)

    def get_month_name():
        month_name = calendar.month_name[date_calculator.get_current_month()]
        
        return(month_name)
        
    def get_current_year():
        current_year = datetime.datetime.now().date().year
        return current_year


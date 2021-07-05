import date_calculator
import organizer
import interface
import file_organizer
import bmi_calculator




user_params = file_organizer.file_organizer.open_config_file()


new_line_data = interface.interface.main_interface(user_params)

today_date = (date_calculator.date_calculator.get_today_date())

current_month = date_calculator.date_calculator.get_current_month()
current_month_name = date_calculator.date_calculator.get_month_name()

current_year = date_calculator.date_calculator.get_current_year()


folder_name = organizer.organizer.monthly_folder_organizer()


file_organizer.file_organizer.open_yearly_file(current_year)

file_organizer.file_organizer.open_monthly_file(folder_name, current_month_name)

new_line_data = str(today_date)+";"+new_line_data[0]+";"+new_line_data[1]+";"+new_line_data[2]+";"+new_line_data[3]+";"+new_line_data[4]+";"+new_line_data[5]+";"+new_line_data[6]+";"+new_line_data[7]+";"+new_line_data[8]

file_organizer.file_organizer.save_monthly_data(new_line_data,folder_name,current_month_name)
file_organizer.file_organizer.save_yearly_data(new_line_data,current_year)
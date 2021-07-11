
import date_calculator
import organizer
import interface
import file_organizer
import bmi_calculator
import data_catcher



user_params = file_organizer.file_organizer.open_config_file()
today_date = (date_calculator.date_calculator.get_today_date())
current_month = date_calculator.date_calculator.get_current_month()
current_month_name = date_calculator.date_calculator.get_month_name()
current_year = date_calculator.date_calculator.get_current_year()
folder_name = organizer.organizer.monthly_folder_organizer()


#open files

file_organizer.file_organizer.open_yearly_file(current_year)
file_organizer.file_organizer.open_monthly_file(folder_name, current_month_name)

#===========


yearly_data = data_catcher.data_catcher.get_yearly_data(current_year)




def main():
    selected_data = interface.interface.main_interface_selector()
    if selected_data == 1:
        new_line_data = interface.interface.main_input_data(user_params)
        new_line_data = str(today_date)+";"+new_line_data[0]+";"+new_line_data[1]+";"+new_line_data[2]+";"+new_line_data[3]+";"+new_line_data[4]+";"+new_line_data[5]+";"+new_line_data[6]+";"+new_line_data[7]+";"+new_line_data[8]
        file_organizer.file_organizer.save_monthly_data(new_line_data,folder_name,current_month_name)
        file_organizer.file_organizer.save_yearly_data(new_line_data,current_year)
        main()

    if selected_data == 2:
        print("Statistics")
        main()

    if selected_data == 3:
        data = yearly_data["Weight(kg)"]
        labels = ["Weight(kg)"]
        print(yearly_data.columns)

        number_days=data_catcher.data_catcher.get_incremental_days_year(current_year)
        limiar_weights = bmi_calculator.bmi_calculator.get_limiar_weights(float(user_params['height']))

        interface.interface.graphic_ploting(data,number_days,labels,limiar_weights)
        main()

main()
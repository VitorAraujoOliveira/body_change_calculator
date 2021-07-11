
from logging import exception
from queue import Empty
from tkinter.ttk import Style
from PySimpleGUI.PySimpleGUI import Button
import pandas as pd
from bmi_calculator import bmi_calculator
import PySimpleGUI as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib








class interface:
    def main_interface_selector():
        layout = [
            [sg.Text('Select option')],
            [sg.Button('Add new measurement',size=(30,3), key='-ADDM-')],
            [sg.Button('Check Statistics',size=(30,3), key='-CHECKS-')],
            [sg.Button('See graphics',size=(30,3), key='-GRAPH-')],
            [sg.Button('Exit',size=(30,3), key='-EXIT-')],
        ]
        window = sg.Window('Body Change Organizer', layout)

        while True:
            event, values = window.read()
            if event == '-EXIT-':
                window.close()
                return 0
                break
            
            if event == '-ADDM-':
                window.close()
                return 1

            if event == '-CHECKS-':
                window.close()
                return 2

            if event == '-GRAPH-':
                window.close()
                return 3



    def main_graph_selector():
        layout = [
            [sg.Text('Select graphic')],
            [sg.Button('Yearly Weight',size=(30,3), key='-ADDM-'),sg.Button('Monthly Weight',size=(30,3), key='-ADDM-'),],
            [sg.Button('Yearly Hip',size=(30,3), key='-ADDM-'),sg.Button('Monthly Weight',size=(30,3), key='-ADDM-'),],
            [sg.Button('Yearly Waist',size=(30,3), key='-ADDM-'),sg.Button('Monthly Weight',size=(30,3), key='-ADDM-'),],
            [sg.Button('Yearly Bust',size=(30,3), key='-ADDM-'),sg.Button('Monthly Weight',size=(30,3), key='-ADDM-'),],
            [sg.Button('Yearly Thighs',size=(30,3), key='-ADDM-'),sg.Button('Monthly Weight',size=(30,3), key='-ADDM-'),],
            [sg.Button('Yearly Biceps',size=(30,3), key='-ADDM-'),sg.Button('Monthly Weight',size=(30,3), key='-ADDM-'),],
            [sg.Button('Yearly Body Fat',size=(30,3), key='-ADDM-'),sg.Button('Monthly Weight',size=(30,3), key='-ADDM-'),],
            [sg.Button('Yearly BMI',size=(30,3), key='-ADDM-'),sg.Button('Monthly Weight',size=(30,3), key='-ADDM-'),],

            [sg.Button('Exit',size=(62,3), key='-EXIT-')],
        ]
        window = sg.Window('Body Change Organizer', layout)

        while True:
            event, values = window.read()
            if event == '-EXIT-':
                window.close()
                return 0
                break
            
            if event == '-ADDM-':
                window.close()
                return 1

            if event == '-CHECKS-':
                window.close()
                return 2

            if event == '-GRAPH-':
                window.close()
                return 3
    


    def open_csv_data():
        sg.set_options(auto_size_buttons=True)
        filename = sg.popup_get_file(
            'filename to open', no_window=True, file_types=(("CSV Files", "*.csv"),))
        # --- populate table with file contents --- #
        if filename == '':
            return

        data = []
        header_list = []
        button = sg.popup_yes_no('Does this file have column names already?')

        if filename is not None:
            try:
                # Header=None means you directly pass the columns names to the dataframe
                df = pd.read_csv(filename, sep=';', engine='python', header=None)
                data = df.values.tolist()               # read everything else into a list of rows
                if button == 'Yes':                     # Press if you named your columns in the csv
                    # Uses the first row (which should be column names) as columns names
                    header_list = df.iloc[0].tolist()
                    # Drops the first row in the table (otherwise the header names and the first row will be the same)
                    data = df[1:].values.tolist()
                elif button == 'No':                    # Press if you didn't name the columns in the csv
                    # Creates columns names for each column ('column0', 'column1', etc)
                    header_list = ['column' + str(x) for x in range(len(data[0]))]
            except exception as error:
                sg.popup_error('Error reading file ')
                return

        layout = [
            [sg.Table(values=data,
                    headings=header_list,
                    display_row_numbers=True,
                    auto_size_columns=False,
                    num_rows=min(25, len(data)))]
        ]

        window = sg.Window('Table', layout, grab_anywhere=False)
        event, values = window.read()
        window.close()




    def main_input_data(user_params):
        layout = [
            [sg.Text('Enter measurements:')],
            [sg.Text('Configured height: '+ user_params['height']+"m")],
            [sg.Text('Weight (kg): '),sg.Input('',size=(18,1), enable_events=True, key='-WEIGHT-', )],
            [sg.Text('Hip  (cm): '),sg.Input('',size=(18,1), enable_events=True, key='-WAIST-', )],
            [sg.Text('Waist  (cm): '),sg.Input('',size=(18,1), enable_events=True, key='-BELLY-', )],
            [sg.Text('Bust   (cm): '),sg.Input('',size=(18,1), enable_events=True, key='-BUST-', )],
            [sg.Text('Thighs (cm): '),sg.Input('',size=(18,1), enable_events=True, key='-THIGHS-', )],
            [sg.Text('Biceps (cm): '),sg.Input('',size=(18,1), enable_events=True, key='-BICEPS-', )],
            [sg.Text('Body Fat(mm): '),sg.Input('',size=(18,1), enable_events=True, key='-BFP-', )],
            [sg.Text('BMI (kg/m²)'), sg.Text(size=(15,1), key='-BMI-')],
            [sg.Text('BMI class'), sg.Text(size=(30,1), key='-BMICLASS-')],

            [sg.Button('Ok',size=(14,1), key='-OK-'), sg.Button('Exit')],
            [sg.Button('Submit',size=(14,1), visible=False, bind_return_key=True)]
            ]

        window = sg.Window('Body Change Organizer', layout)

        while True: # Event Loop
            event, values = window.read()


            if not values['-WEIGHT-'] == '':
                window['-BMI-'].update(bmi_calculator.get_bmi(float(user_params['height']),float(values['-WEIGHT-'])))
                window['-BMICLASS-'].update(bmi_calculator.get_ranges(float(user_params['height']),float(values['-WEIGHT-'])))
            else:
                window['-BMI-'].update('')
                window['-BMICLASS-'].update('')

            if event in (None, 'Exit'):
                break
            # if last char entered not a digit
            if len(values['-WEIGHT-']) and values['-WEIGHT-'][-1] not in ('0123456789.'):
                window['-WEIGHT-'].update(values['-WEIGHT-'][:-1])


            if len(values['-WAIST-']) and values['-WAIST-'][-1] not in ('0123456789.'):
                window['-WAIST-'].update(values['-WAIST-'][:-1])


            if len(values['-BELLY-']) and values['-BELLY-'][-1] not in ('0123456789.'):
                window['-BELLY-'].update(values['-BELLY-'][:-1])


            if len(values['-BUST-']) and values['-BUST-'][-1] not in ('0123456789.'):
                window['-BUST-'].update(values['-BUST-'][:-1])


            if len(values['-THIGHS-']) and values['-THIGHS-'][-1] not in ('0123456789.'):
                window['-THIGHS-'].update(values['-THIGHS-'][:-1])


            if len(values['-BICEPS-']) and values['-BICEPS-'][-1] not in ('0123456789.'):
                window['-BICEPS-'].update(values['-BICEPS-'][:-1])

            if len(values['-BFP-']) and values['-BFP-'][-1] not in ('0123456789.'):
                window['-BFP-'].update(values['-BFP-'][:-1])


            elif event == 'Submit':
                print('Weight(kg): %s'% window['-WEIGHT-'].get())
                print('Waist(cm): %s'% window['-WAIST-'].get())
                print('Belly(cm): %s'% window['-BELLY-'].get())
                print('Bust %s'% window['-BUST-'].get())
                print('Thighs %s'% window['-THIGHS-'].get())
                print('Biceps %s'% window['-BICEPS-'].get())
                print('Body fat measurement %s'% window['-BFP-'].get())

            elif event == '-OK-':

                final_csv = (
                    values['-WEIGHT-'],
                    values['-WAIST-'],
                    values['-BELLY-'],
                    values['-BUST-'],
                    values['-THIGHS-'],
                    values['-BICEPS-'],
                    values['-BFP-'],
                    window['-BMI-'].get(),
                    window['-BMICLASS-'].get(),)

                return final_csv

                

    def graphic_ploting(data,time,labels,limiars):
        fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
        import matplotlib.pyplot as plt



        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(time,data,label=labels[0])


        if not limiars == None:
            ax.hlines(y=limiars[0], xmin=time[0], xmax=len(time)-1, colors='g', linestyles='--', lw=1,label="ideal weight")
            
            if (limiars[1] - data[len(data)-1]) > 15:
                ax.hlines(y=limiars[5], xmin=time[0], xmax=len(time)-1, colors='blue', linestyles='--', lw=1,label="underweight line")
            if (limiars[1] - data[len(data)-1]) < 15:
                ax.hlines(y=limiars[1], xmin=time[0], xmax=len(time)-1, colors='lightcoral', linestyles='--', lw=1,label="overweight line")

            if (limiars[2] - data[len(data)-1]) < 15:
                ax.hlines(y=limiars[2], xmin=time[0], xmax=len(time)-1, colors='tomato', linestyles='--', lw=1,label="Obesity line")

            if (limiars[3] - data[len(data)-1]) < 15:
                ax.hlines(y=limiars[3], xmin=time[0], xmax=len(time)-1, colors='firebrick', linestyles='--', lw=1,label="Sever Obesity line")

            if (limiars[4] - data[len(data)-1]) < 15:
                ax.hlines(y=limiars[4], xmin=time[0], xmax=len(time)-1, colors='maroon', linestyles='--', lw=1,label="Morbid obesity line")


        plt.legend()
        ax.set_xlabel('Time (days)')

        # Define the window layout
        layout = [
            [sg.Text("Plot test")],
            [sg.Canvas(key="-CANVAS-")],
            [sg.Button("Ok",key='-OK-'),sg.Button("Detail graph", key='-DETAIL-')],
        ]
        matplotlib.use("TkAgg")

        def draw_figure(canvas, figure):
            figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
            figure_canvas_agg.draw()
            figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
            return figure_canvas_agg
        # Create the form and show it without the plot
        window = sg.Window(
            "Matplotlib Single Graph",
            layout,
            location=(0, 0),
            finalize=True,
            element_justification="center",
            font="Helvetica 18",
        )

        # Add the plot to the window
        draw_figure(window["-CANVAS-"].TKCanvas, fig)

        while True:
            event, values = window.read()
            if event == '-OK-':
                window.close()
                break
            elif event == '-DETAIL-':
                plt.show()
                plt.close()
                window.close()
                break



interface.main_graph_selector()
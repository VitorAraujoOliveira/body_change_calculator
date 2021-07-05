
from bmi_calculator import bmi_calculator
import PySimpleGUI as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib








class interface:
    def main_interface(user_params):
        layout = [
            [sg.Text('Enter measurements:')],
            [sg.Text('Configured height: '+ user_params['height']+"m")],
            [sg.Text('Weight (kg): '),sg.Input('',size=(18,1), enable_events=True, key='-WEIGHT-', )],
            [sg.Text('Waist  (cm): '),sg.Input('',size=(18,1), enable_events=True, key='-WAIST-', )],
            [sg.Text('Belly  (cm): '),sg.Input('',size=(18,1), enable_events=True, key='-BELLY-', )],
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

                

    def graphic_interface():
        fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))


        # Define the window layout
        layout = [
            [sg.Text("Plot test")],
            [sg.Canvas(key="-CANVAS-")],
            [sg.Button("Ok")],
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

        event, values = window.read()

        window.close()








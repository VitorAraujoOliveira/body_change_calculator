import math




class bmi_calculator:

    def get_bmi(height, weight):
        bmi = weight/(height**2)
        return(bmi)
    
    def get_ranges(height, weight):
        range = ""
        bmi = bmi_calculator.get_bmi(height, weight)

        if(bmi < 18.5):
            range = "Underweight"
        elif(18.5 < bmi < 24.9):
            range = "Recommended weight"
        elif(25 < bmi < 29.9):
            range = "Overweight"
        elif(30 < bmi < 34.9):
            range = "Obese"
        elif(35 < bmi < 39.9):
            range = "Severely Obese"
        elif(bmi > 40):
            range = "Morbidly Obese"
        
        return range


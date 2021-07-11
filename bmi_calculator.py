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

    def get_limiar_weights(height):
        morbidly_obesity_limiar = 40 * (height**2)
        severe_obesity_limiar = 35 * (height**2)
        obesity_limiar = 30 * (height**2)
        overweight_limiar = 25 * (height**2)
        ideal_weight_limiar = 21.5 * (height**2)
        underweight_limiar = 18.5 * (height**2)

        return [ideal_weight_limiar,overweight_limiar,obesity_limiar,severe_obesity_limiar,morbidly_obesity_limiar,underweight_limiar]
    
